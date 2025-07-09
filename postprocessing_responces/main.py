import re
import pandas as pd

# --- 1) Load the Excel file ---
df = pd.read_excel("DATA.xlsx", sheet_name="Sheet0")
print("Number of columns:", df.shape[1])
print("Number of rows:", df.shape[0])

# --- 2) Build a dictionary keyed by participant ---
participants = {}
for idx, row in df.iterrows():
    participants[row["ResponseId"]] = row.to_dict()

# --- 3) Define attributes to remove & create a cleaned dict ---
attrs_to_remove = [
    "EndDate","ExternalReference","DistributionChannel","Finished","IPAddress",
    "LocationLatitude","LocationLongitude","Progress","PROLIFIC_PID","RecordedDate",
    "ResponseId","StartDate","Status","UserLanguage","Q1.3_Consent","Q1.4","Q1.5_Consent",
    "Q1.6_Consent","Q1.7_Consent","Q2.1_Prolific ID"
]

participants_cleaned = {}
new_id = 1
for idx, row in df.iloc[1:].iterrows():
    row_dict = row.to_dict()
    cleaned_data = {
        k: v
        for k, v in row_dict.items()
        if pd.notna(v)
           and k not in attrs_to_remove
           and "Click Count" not in k
           and "First Click" not in k
           and "Last Click" not in k
    }
    participants_cleaned[new_id] = cleaned_data
    new_id += 1

# --- 4) Rename keys that start with 'Q3.' and contain 'Training' -> 'Instructions' ---
for pid, data in participants_cleaned.items():
    updated = {}
    for k, v in data.items():
        if k.startswith("Q3.") and "Training" in k:
            new_key = k.replace("Training", "Instructions")
            updated[new_key] = v
        else:
            updated[k] = v
    participants_cleaned[pid] = updated

# --- 5) Stage classification ---
def get_stage_substage(col_name):
    if "Instructions" in col_name:
        return ("Instructions", None)
    if "Rainbow" in col_name:
        return ("Experiment", "Training")
    m = re.match(r'^(Q[4-9])\.(\d+)', col_name)
    if m:
        qnum = int(m.group(2))
        if qnum <= 143:
            return ("Experiment", "Pre-Training")
        elif qnum >= 155:
            return ("Experiment", "Post-Training")
        else:
            return ("Experiment", "Training")
    return ("Experiment", "Training")

participants_by_stage = {}
for pid, pdata in participants_cleaned.items():
    st = {
        "Instructions": {},
        "Experiment": {
            "Pre-Training": {},
            "Training": {},
            "Post-Training": {}
        }
    }
    for col_name, col_val in pdata.items():
        main, sub = get_stage_substage(col_name)
        if main == "Instructions":
            st["Instructions"][col_name] = col_val
        else:
            st["Experiment"][sub][col_name] = col_val
    participants_by_stage[pid] = st

# --- 6) Move "Duration (in seconds)" -> top-level "Total Survey Duration" ---
for pid, st in participants_by_stage.items():
    val = st["Instructions"].pop("Duration (in seconds)", None)
    if val is None:
        for sb in ["Pre-Training", "Training", "Post-Training"]:
            if "Duration (in seconds)" in st["Experiment"][sb]:
                val = st["Experiment"][sb].pop("Duration (in seconds)")
                break
    if val is not None:
        st["Total Survey Duration"] = val

# --- 7) Subdivide 'Instructions' into 4 subgroups (Q3.X_) ---
pat_q3 = re.compile(r'^Q3\.(\d+)_')
for pid, st in participants_by_stage.items():
    old_instr = st["Instructions"]
    new_instr = {
        "The young girl gave no clear response": {},
        "Kittens": {},
        "Seven": {},
        "Lift the square stone over the fence": {}
    }
    for k, v in old_instr.items():
        m = pat_q3.match(k)
        if m:
            n = int(m.group(1))
            if   4 <= n <= 11:
                new_instr["The young girl gave no clear response"][k] = v
            elif 13 <= n <= 19:
                new_instr["Kittens"][k] = v
            elif 21 <= n <= 27:
                new_instr["Seven"][k] = v
            elif 29 <= n <= 35:
                new_instr["Lift the square stone over the fence"][k] = v
    st["Instructions"] = new_instr

# --- 8) Rename the *inner* question keys (like "Response"), preserving original question. ---
for pid, st in participants_by_stage.items():
    instr_sub = st["Instructions"]
    for section, sec_data in instr_sub.items():
        old_keys = sorted(sec_data.keys())
        if section == "The young girl gave no clear response":
            if len(old_keys) != 4:
                continue
            new_order = ["Response","Naturalness","Speaker Effort","Listener Effort"]
        else:
            if len(old_keys) != 5:
                continue
            new_order = ["Response","Duration","Naturalness","Speaker Effort","Listener Effort"]
        
        renamed = {}
        for old_k, new_k in zip(old_keys, new_order):
            renamed[new_k] = {
                "value": sec_data[old_k],
                "original_question": old_k
            }
        sec_data.clear()
        sec_data.update(renamed)

# --- 8a) Now rename the *four sections* themselves to "Block1..4" and store their old name as "Description". ---
section_renames = {
    "The young girl gave no clear response": "Block1",
    "Kittens": "Block2",
    "Seven": "Block3",
    "Lift the square stone over the fence": "Block4"
}

for pid, st in participants_by_stage.items():
    old_instr = st["Instructions"]
    new_instr = {}
    for old_section_name, section_data in old_instr.items():
        if old_section_name in section_renames:
            new_block_name = section_renames[old_section_name]
            section_data["Description"] = old_section_name
            new_instr[new_block_name] = section_data
        else:
            new_instr[old_section_name] = section_data
    st["Instructions"] = new_instr

# --- 9) Remove "Q3.5_Page Submit" from Training ---
for pid, st in participants_by_stage.items():
    st["Experiment"]["Training"].pop("Q3.5_Page Submit", None)

# --- 10) Group Experiment Pre-Training/Post-Training keys by patterns ---
patterns = [
    "Banana","Physician","Vegetables","Watch","Aluminum","Statistics","Butterfly",
    "Judge","Computer","Rhinoceros","Specific","Shipwreck","Elephant","Newspaper",
    "Potato","Stethoscope","Volcano","Animals"
]
for pid, st in participants_by_stage.items():
    for sb in ["Pre-Training","Post-Training"]:
        old_data = st["Experiment"][sb]
        new_data = {}
        for k, v in old_data.items():
            for pat in patterns:
                if pat in k:
                    new_data.setdefault(pat, {})[k] = v
                    # If not set, store the base pattern in "Description" so we
                    # keep the original name
                    if "Description" not in new_data[pat]:
                        new_data[pat]["Description"] = pat
                    break
        st["Experiment"][sb] = new_data

# --- 11) For any pattern w/ 18 items in Pre-Training, split into first 9 vs. last 9,
#     ensuring we sort by numeric suffix rather than a naive alphabetical sort.

def numeric_suffix_sort(k):
    match = re.search(r'\.(\d+)_', k)
    if match:
        return int(match.group(1))
    return 999999

for pid, st in participants_by_stage.items():
    pre_dict = st["Experiment"]["Pre-Training"]
    new_patts = {}
    for pat_name, pat_data in pre_dict.items():
        # Exclude 'Description' from the count
        qkeys = [x for x in pat_data if x != "Description"]
        if len(qkeys) == 18:
            sorted_keys = sorted(qkeys, key=numeric_suffix_sort)
            first9, last9 = sorted_keys[:9], sorted_keys[9:]
            cons_name = pat_name + "_consistency"
            cons_dict = {}
            for k in last9:
                cons_dict[k] = pat_data[k]
                del pat_data[k]
            # Also copy the base "Description"
            if "Description" in pat_data:
                cons_dict["Description"] = pat_data["Description"]
            new_patts[cons_name] = cons_dict
    pre_dict.update(new_patts)

# --- 12) For 9-item patterns in pre/post, rename question-level keys w/ new_labels, skipping 3rd, storing original question
new_labels = [
    "Total Duration","Response","Time to listen and type the answer",
    "Time spent evaluating Naturalness","Naturalness Rating",
    "Time spent evaluating speaker effort","Speaker Effort",
    "Time spent evaluating listener effort","Listener Effort"
]

def numeric_suffix_sort(k):
    m = re.search(r'\.(\d+)_', k)
    return int(m.group(1)) if m else 9999

for pid, st in participants_by_stage.items():
    for sb in ["Pre-Training","Post-Training"]:
        for pat_name, old_qdict in st["Experiment"][sb].items():
            qkeys = [x for x in old_qdict if x != "Description"]
            if len(qkeys) == 9:
                sorted_qkeys = sorted(qkeys, key=numeric_suffix_sort)
                new_q = {}
                for old_k, label in zip(sorted_qkeys, new_labels):
                    if label == "Time to listen and type the answer":
                        continue
                    new_q[label] = {
                        "value": old_qdict[old_k],
                        "original_question": old_k
                    }
                desc = old_qdict.get("Description", pat_name)
                old_qdict.clear()
                old_qdict["Description"] = desc
                old_qdict.update(new_q)

print("\n=== All transformations complete. ===")

#
# STEP 13) Rename Pre-Training and Post-Training patterns 
#           to "<index>_<Description>" or "<index>_<Description>_consistency"
#           using the numeric question order.
#

def min_question_number_in_pattern(pattern_dict):
    """
    Return the smallest integer suffix from question keys, e.g. Q4.171 => 171.
    Skip the 'Description' key.
    """
    min_val = 999999
    for k in pattern_dict.keys():
        if k == "Description":
            continue
        match = re.search(r'\.(\d+)_', k)
        if match:
            num = int(match.group(1))
            if num < min_val:
                min_val = num
    return min_val

for pid, st in participants_by_stage.items():
    for sb in ["Pre-Training", "Post-Training"]:
        old_dict = st["Experiment"][sb]  # e.g. { "Banana": { "Description":"Banana", ...}, ... }
        
        # 1) Gather (pattern_key, pattern_data, min_num)
        pattern_list = []
        for pattern_key, pattern_data in old_dict.items():
            mnum = min_question_number_in_pattern(pattern_data)
            pattern_list.append((pattern_key, pattern_data, mnum))

        # 2) Sort by numeric suffix
        pattern_list.sort(key=lambda x: x[2])

        new_dict = {}
        block_index = 1
        for (pattern_key, pat_data, _) in pattern_list:
            # We'll rely on pat_data["Description"] if it exists; otherwise fallback to pattern_key
            base_name = pat_data.get("Description", pattern_key)
            # If pattern_key ends w/ "_consistency", rename final key => "1_Banana_consistency"
            if pattern_key.endswith("_consistency"):
                # remove the existing "_consistency" from base_name if it was appended
                # so we don't get double. Example: base_name= "Banana_consistency" => "Banana"
                if base_name.endswith("_consistency"):
                    base_name = base_name[:-12]
                
                final_key = f"{block_index}_{base_name}_consistency"
                pat_data["Description"] = base_name  # keep desc as "Banana" 
            else:
                final_key = f"{block_index}_{base_name}"
                pat_data["Description"] = base_name

            new_dict[final_key] = pat_data
            block_index += 1

        st["Experiment"][sb] = new_dict


import re

# Define a map from (numStr, hasPageSubmitBool) -> new label
rainbow_map = {
    ("148", True):  "Time spent evaluating Naturalness",
    ("149", False): "Naturalness Rating",
    ("150", True):  "Time spent evaluating speaker effort",
    ("151", False): "Speaker Effort Rating",
    ("152", True):  "Time spent evaluating listener effort",
    ("153", False): "Listener Effort Rating"
}
# 145 -> remove entirely

def parse_rainbow_training_key(keyname):
    """
    Attempt to match something like:
       Q[4-9].145_Rainbow_Page Submit
    or Q8.149_Rainbow, etc.

    Return a tuple (numStr, hasPageSubmit), e.g. ("149", False)
    Or ("145", True) if it ends with _Page Submit
    If it doesn't match the pattern, return (None, None).
    """
    # Example patterns to match:
    #  Q4.148_Rainbow_Page Submit
    #  Q6.149_Rainbow
    pat = re.compile(r'^Q[4-9]\.(\d+)_Rainbow(?:_Page Submit)?$')
    match = pat.match(keyname)
    if match:
        num = match.group(1)  # the numeric portion, e.g. 148
        # Check if we ended with "Page Submit"
        hasPage = ("Page Submit" in keyname)
        return (num, hasPage)
    return (None, None)

for pid, st in participants_by_stage.items():
    training_dict = st["Experiment"]["Training"]  # { old_key: value, ... }

    new_training = {}
    for old_key, old_val in training_dict.items():
        num_str, has_page = parse_rainbow_training_key(old_key)

        if num_str is not None:
            # remove Q..145
            if num_str == "145":
                continue
            if (num_str, has_page) in rainbow_map:
                new_label = rainbow_map[(num_str, has_page)]
                new_training[new_label] = {
                    "value": old_val,
                    "original_question": old_key
                }
            else:
                # skip or keep as is
                continue
        else:
            new_training[old_key] = old_val

    st["Experiment"]["Training"] = new_training

print("\n=== Completed renaming. No double '_consistency' appended! ===")





# SAVING DATA
import json

# Suppose your final data structure is 'participants_by_stage'

output_filename = "organized_data.json"

with open(output_filename, "w", encoding="utf-8") as f:
    json.dump(participants_by_stage, f, ensure_ascii=False, indent=2)

print(f"Data saved to {output_filename}")





# Load the JSON file we previously saved
with open("organized_data.json", "r", encoding="utf-8") as f:
    loaded_data = json.load(f)

# Quick check: print the total number of participants
print("Number of participants (keys) in loaded data:", len(loaded_data))

# Optionally, peek at the first participant ID and its structure
first_pid = next(iter(loaded_data))  # gets the first key in the dict
print("First participant ID:", first_pid)
print("Keys at top level for this participant:", list(loaded_data[first_pid].keys()))

# You can also drill down further:
print("\nExperiment substructure for first participant:", loaded_data[first_pid]["Experiment"].keys())


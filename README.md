# The More You Listen, The More You Understand: Perception and Progression in PPAOS

## Overview

This repository contains experimental materials, custom scripts, and data post-processing pipelines from my research on **Primary Progressive Apraxia of Speech (PPAOS)** – a neurodegenerative motor speech disorder characterized by impaired speech planning and programming. The research integrates my dual interests in **speech science and computational data analysis** and combines clinical research questions with python/javascript programming.

The study aimed to understand how **listener perception of an individual with PPAOS changes over time**, and whether **brief familiarization training** can improve intelligibility, reduce perceived effort, and enhance communication quality.

---

## Motivation


While treatment for PPAOS traditionally focuses on the speaker, communication is inherently **bidirectional**. Improving listener adaptation and perception can reduce the communicative burden on the speaker, potentially enhancing quality of life for individuals with progressive motor speech disorders.
![image](https://github.com/user-attachments/assets/8411aae9-24fa-4e5d-b711-5d6b4e8715ed)
---

## Research Design

- **Participants**: Listened to and transcribed speech samples recorded from an individual with PPAOS.
- **Three Phases**:
  - **Pre-training**: Baseline transcription and perceptual ratings.
  - **Training**: Familiarization with written transcriptions alongside audio.
  - **Post-training**: Reassessment of transcription accuracy and perceptual ratings.

![image](https://github.com/user-attachments/assets/8821eecf-1b21-4a57-b13c-8262b590a75c)

### Data Collected

- **Transcriptions** of words and sentences.
- **Ratings** - ***
- **Response durations** to assess processing time.

---

## Repository Contents

| File/Folder | Description |
|-------------|-------------|
| `main.py` | Python script to transform Qualtrics raw outputs (Excel format) into a structured JSON (`organized_data.json`). It cleans, organizes, and hierarchically groups participant data by experimental stage, facilitating efficient analysis. |
| `organized_data.json` | Example output file storing all experimental data in an object-oriented, cross-platform compatible format. |
| `sample*.html`, `sample*.js` | Custom HTML and JavaScript code snippets embedded within Qualtrics to implement experimental controls such as one-time audio playback, hidden input reveals upon audio completion, and precise response timing. |
| `README.md` | This file. Provides project overview and documentation. |

---

## Key Implementation Highlights

**Advanced Data Processing**  
The `main.py` script processes datasets with over **1400 participants and 200+ variables each**, outputting them into clean JSON structures categorized by participant, phase, and task for immediate analysis.

**Custom Qualtrics Integration**  
Includes JavaScript and HTML codes to:
- Restrict audio to single playback per trial (emulating natural conversation conditions).
- Record precise timing for user interactions.
- Dynamically reveal transcription inputs post audio completion, ensuring experimental validity.

**Object-Oriented Data Design**  
Transforms flat .csv/.xlsx outputs into hierarchical JSON for **efficient data querying, visualization, and statistical modeling**.


---

## References

1. **Davydzenka, V.** (2025). *The More You Listen, The More You Understand: Perception and Progression in PPAOS*. Oral Presentation at INBRE Research Conference and Poster Presentation at Undergraduate Research & Inquiry Day, University of Wyoming.

---

## Contact

For further details, dataset requests, or collaboration inquiries:

**Viyaleta Davydzenka**  
Email: [vdavydze@uwyo.edu](mailto:vdavydze@uwyo.edu)

---

## Acknowledgements


I would like to thank **Dr. Kriegel**  at **University of Wyoming** for all her help and guidance throughout the project.

*** - More information will be published after research is presented at an upcomming ASHA Conference in Washington DC, 2026.

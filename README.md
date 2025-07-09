# ppaos_research
The following code was developed as a part of a project aimed at studying Progressive Primary Apraxia of Speech (PPAOS).
"The More You Listen, The More You Understand: Perception and Progression in PPAOS"


Primary Progressive Apraxia of Speech (PPAOS) is a neurodegenerative motor speech disorder. It is characterized by impaired planning or programming of movements. Because PPAOS is a progressive disorder, its symptoms worsen over time.
![image](https://github.com/user-attachments/assets/08006c1f-605c-4190-8bdf-a6c624d2ac16)



Link to research and all the relevant inf .




The "creating_questionnaire" folder stores some of the custom sample questions that were created for Qualtrics.
The folder titled "postprocessing_responces" stores a python file main.py, which is used to organize raw and cumbersome output from Qualtrics (consisting of 1400 x 200 data entries), into a simple organized_data.json file, that groups  all data in an object-oriented manner (using a hashmap), where each experiment hashmap stores participants (keys) and their responces (values). The resulting output JSON file is cross-platform (can be imported by most software and coding languages) and makes it extremely easy to analyze large datasets, by storing entire data in a hirerachical structure (as opposed to collumn-row based way, as in .csv files).

Please feel free to adapt the codes for your own experiments in Qualtrics or reach out at my email (vdavydze at uwyo . edu) for complete dataset and HTML + Javascript codes for the entire questionnaire. 

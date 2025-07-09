The following code was developed as a part of a project aimed at studying Progressive Primary Apraxia of Speech (PPAOS).
"The More You Listen, The More You Understand: Perception and Progression in PPAOS"


Primary Progressive Apraxia of Speech (PPAOS) is a neurodegenerative motor speech disorder. It is characterized by impaired planning or programming of movements. Because PPAOS is a progressive disorder, its symptoms worsen over time. Treatment typically focuses on the speaker, but both the speaker and listener contribute to successful communication. Enhancing listener capabilities can reduce the burden on the speaker and improve communication quality. This study quantified changes in listener perception of a speaker with PPAOS over an 8-month period and examined whether brief training could improve listeners’ ability to understand the speech.
![image](https://github.com/user-attachments/assets/8411aae9-24fa-4e5d-b711-5d6b4e8715ed)





Link to research and all the relevant inf .




The "creating_questionnaire" folder stores some of the custom sample questions that were created for Qualtrics.
The folder titled "postprocessing_responces" stores a python file main.py, which is used to organize raw and cumbersome output from Qualtrics (consisting of 1400 x 200 data entries), into a simple organized_data.json file, that groups  all data in an object-oriented manner (using a hashmap), where each experiment hashmap stores participants (keys) and their responces (values). The resulting output JSON file is cross-platform (can be imported by most software and coding languages) and makes it extremely easy to analyze large datasets, by storing entire data in a hirerachical structure (as opposed to collumn-row based way, as in .csv files).

Please feel free to adapt the codes for your own experiments in Qualtrics or reach out at my email (vdavydze at uwyo . edu) for complete dataset and HTML + Javascript codes for the entire questionnaire. 

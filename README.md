The following code was developed as a part of a project aimed at studying Progressive Primary Apraxia of Speech (PPAOS).
"The More You Listen, The More You Understand: Perception and Progression in PPAOS"


About:
Primary Progressive Apraxia of Speech (PPAOS) is a neurodegenerative motor speech disorder. It is characterized by impaired planning or programming of movements. Because PPAOS is a progressive disorder, its symptoms worsen over time. Treatment typically focuses on the speaker, but both the speaker and listener contribute to successful communication. Enhancing listener capabilities can reduce the burden on the speaker and improve communication quality. This study quantified changes in listener perception of a speaker with PPAOS over an 8-month period and examined whether brief training could improve listeners’ ability to understand the speech.
![image](https://github.com/user-attachments/assets/8411aae9-24fa-4e5d-b711-5d6b4e8715ed)



Research Design:
The experiment included three phases: pre-training, training, and post-training.
Participants listened to, transcribed, and rated speech samples from an individual with PPAOS.
During the training phase, participants listened to speech while following along with written transcription, helping them familiarize with the speaker’s impaired speech.
![image](https://github.com/user-attachments/assets/8821eecf-1b21-4a57-b13c-8262b590a75c)





Results:
After brief familiarization, listeners rated both their own effort and the speaker’s effort as lower, suggesting that the speech became easier to understand and seemed less difficult to produce.
Ratings of naturalness increased from pre- to post-training for both words and sentences, showing that speech was perceived as more natural after exposure.
For word stimuli, naturalness ratings decreased over time, reflecting listeners’ ability to detect the progression of speech degradation as the disease advanced.
![image](https://github.com/user-attachments/assets/2d99e4ee-4b4d-4735-bfcd-7377541c33c0)


Significance of the Study:
The findings suggest that while communication declines with disease progression, listener familiarization can help maintain communication quality.




Link to research and all the relevant inf .




The "creating_questionnaire" folder stores some of the custom sample questions that were created for Qualtrics.
The folder titled "postprocessing_responces" stores a python file main.py, which is used to organize raw and cumbersome output from Qualtrics (consisting of 1400 x 200 data entries), into a simple organized_data.json file, that groups  all data in an object-oriented manner (using a hashmap), where each experiment hashmap stores participants (keys) and their responces (values). The resulting output JSON file is cross-platform (can be imported by most software and coding languages) and makes it extremely easy to analyze large datasets, by storing entire data in a hirerachical structure (as opposed to collumn-row based way, as in .csv files).

Please feel free to adapt the codes for your own experiments in Qualtrics or reach out at my email (vdavydze at uwyo . edu) for complete dataset and HTML + Javascript codes for the entire questionnaire. 

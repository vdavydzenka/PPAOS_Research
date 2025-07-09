Qualtrics.SurveyEngine.addOnload(function() {
    // 1) Record the start time (in ms) when this page loads
    var startTime = new Date().getTime();
    Qualtrics.SurveyEngine.setEmbeddedData("StartTime_Page1_1", startTime);
});

Qualtrics.SurveyEngine.addOnUnload(function() {
    // 2) Record the end time (in ms) when leaving this page
    var endTime = new Date().getTime();

    // 3) Retrieve the stored start time
    var startTime = parseInt(Qualtrics.SurveyEngine.getEmbeddedData("StartTime_Page1_1"));

    // 4) Calculate total time spent (in ms)
    var timeSpent = endTime - startTime;

    // 5) Save it as an Embedded Data field
    Qualtrics.SurveyEngine.setEmbeddedData("TimeSpent_Page1_1", timeSpent);
});

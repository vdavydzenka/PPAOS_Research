Qualtrics.SurveyEngine.addOnload(function() {
    // Get this question's HTML element
    var qid = this.questionId;
    var questionDiv = document.getElementById("QID" + qid);

    // The question body contains all answer controls, including sliders
    var questionBody = questionDiv.querySelector(".QuestionBody");

    // Get the audio element we placed in the Question Text
    var audio = questionDiv.querySelector("audio");

    if (audio && questionBody) {
        // Hide the sliders until the audio ends
        questionBody.style.display = "none";

        // When the audio finishes, show the sliders
        audio.addEventListener("ended", function() {
            questionBody.style.display = "block";
        });
    }
});

Qualtrics.SurveyEngine.addOnReady(function() {
    // Not used here, but available if needed
});

Qualtrics.SurveyEngine.addOnUnload(function() {
    // Not used here, but available if needed
});

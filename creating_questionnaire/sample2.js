Qualtrics.SurveyEngine.addOnload(function() {
    var that = this;
    var qid = that.questionId;

    // 1. Check if the audio is already finished in this session
    if (sessionStorage.getItem("page1AudioFinished") === "true") {
        // If yes, show the text fields right away
        jQuery("#"+qid+" .InputText").show();
    } else {
        // Otherwise, hide them until the audio ends
        jQuery("#"+qid+" .InputText").hide();
    }

    // 2. Listen for the audio "ended" event
    //    (Assuming there's exactly one <audio> on this page. If more, adjust your selector.)
    jQuery('audio').on('ended', function() {
        // Mark that the audio has finished in sessionStorage
        sessionStorage.setItem("page1AudioFinished", "true");
        // Reveal the text input fields
        jQuery("#"+qid+" .InputText").show();
    });
});

Qualtrics.SurveyEngine.addOnReady(function() {
    // Runs when question is fully rendered
});

Qualtrics.SurveyEngine.addOnUnload(function() {
    // Runs when leaving the page (not used here)
});

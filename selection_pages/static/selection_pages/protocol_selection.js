console.log('Protocol selection page is loaded')

const elements = [...document.getElementsByClassName("ans")]

var protocol_submit_button = document.getElementById('protocol_select_button');
protocol_submit_button.onclick = function(event){
    console.log(event)

    // find the radiobutton that was selected 
    elements.forEach(el => {
        // check if the radio button has been checked for (question, answer)
        if (el.checked){
            console.log('selected : ' + el.value)

            // perform url redirection based on the protocol selected
            selected = el.value;

            // These values are being hard-coded for the moment -- but they will be corrected later
            if (selected == "lipread_words"){
                location.href = '/quizzes/lipread_sentences/1'
            } else if (selected == "lipread_sentences"){
                location.href = '/quizzes/lipread_sentences/3'
            } else if (selected == "lipread_missing"){
                location.href = '/quizzes/lipread_missing/1'
            }
        }
    })
}
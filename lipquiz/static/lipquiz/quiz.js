console.log("Inside the quiz view")
const url = window.location.href
const quizBox = document.getElementById('quiz-box')

// loads the video quiz that was selected
$.ajax({
    type: 'GET',
    url: `${url}data`,
    success: function(response){
        console.log(response)
        data = response.data
        data.forEach(element => {
            for (const [question, answers] of Object.entries(element)){
                // console.log(question)
                quizBox.innerHTML += `
                    <hr>
                    <div class="mb-2">
                        <b>${question}</b>
                    </div>

                    <div class="mb-2">
                        <video width="320" height="240" controls>
                            <source src="/media/${question}" type="video/mp4">
                        </video>
                    </div>
                `
                
                answers.forEach(answer => {
                    quizBox.innerHTML += `
                        <div>
                            <input type="radio" class="ans" id="${question}-${answer}" name="${question}" value="${answer}" >
                            <label for="${question}">${answer}</label>
                        </div>
                    `
                })
            }
        });
    },
    error: function(error){
        console.log(error)
    }
})
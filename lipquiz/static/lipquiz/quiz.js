console.log("Inside the quiz view")
const url = window.location.href
const quizBox = document.getElementById('quiz-box')
const quizForm = document.getElementById('quiz-form')
const scoreBox = document.getElementById('score-box')
const resultBox = document.getElementById('result-box')

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

const csrfToken = document.getElementsByName('csrfmiddlewaretoken')

const sendData = () => {
    const data = {}
    data['csrfmiddlewaretoken'] = csrfToken[0].value
    const elements = [...document.getElementsByClassName("ans")]
    elements.forEach(el => {
        // check if the radio button has been checked for (question, answer)
        if (el.checked){
            data[el.name] = el.value
        }
        else {
            if(!data[el.name]){
                data[el.name] = null
            }
        }
    })

    // make the ajax post request with the data 
    $.ajax({
        type: 'POST',
        url: `${url}save/`,
        data: data,
        success: function(response){
            scoreBox.innerHTML = `Congratulations! Your score is ${response.score}%.`
            const results = response.results 
            quizForm.classList.add('not-visible')
            results.forEach(res => {
                const resDiv = document.createElement("div")
                for (const [question, resp] of Object.entries(res)){
                    // console.log(question)
                    // console.log(resp)

                    resDiv.innerHTML += question
                    const cls = ['container', 'p-3', 'text-light', 'h6']
                    resDiv.classList.add(...cls)

                    const correct = resp['correct_answer']
                    const answered = resp['answered']

                    if (correct == answered){
                        resDiv.classList.add('bg-success')
                        resDiv.innerHTML += ` | answered: ${answered}`
                    } else {
                        resDiv.classList.add('bg-danger')
                        resDiv.innerHTML += ` | answered: ${answered}`
                        resDiv.innerHTML += ` | correct: ${correct}`
                    }
                }

                // const body = document.getElementsByTagName('BODY')[0]
                resultBox.append(resDiv)
            })
        },
        error: function(error){
            console.log(error)
        }
    })
}

quizForm.addEventListener('submit', e => {
    e.preventDefault()
    console.log("Tried submitting the form")

    sendData()
})
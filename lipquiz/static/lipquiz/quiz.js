const url = window.location.href
const quizBox = document.getElementById('quiz-box')
const quizForm = document.getElementById('quiz-form')
const scoreBox = document.getElementById('score-box')
const resultBox = document.getElementById('result-box')
const timeBox = document.getElementById('time-box')
const replaysBox = document.getElementById('replays-box')

// record the time taken on the quiz 
const activateTimer = () => {
    startTime = new Date();
}

// loads the video quiz that was selected
$.ajax({
    type: 'GET',
    url: `${url}data`,
    success: function(response){
        var counter = 1
        response.forEach(element => {
            quizBox.innerHTML += `
                <hr>
                <div class="mb-2">
                    <b>${counter}. ${element.question}</b>
                </div>

                <div class="mb-2">
                    <video width="320" height="240" controls muted>
                        <source src="/media/${element.video_path}" type="video/mp4">
                    </video>
                </div>
            `
            element.answer.forEach(choice => {
                quizBox.innerHTML += `
                    <div>
                        <input type="radio" class="ans" id="${element.video_path}-${choice}" name="${element.video_path}" value="${choice}" >
                        <label for="${element.video_path}">${choice}</label>
                    </div>
                `
            });

            counter += 1
        })

        // start the time after everything is successfully loaded 
        activateTimer()
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
            var counter = 1
            scoreBox.innerHTML = `Your score is ${response.score}%.`
            const results = response.results 
            quizForm.classList.add('not-visible')
            results.forEach(res => {
                const resDiv = document.createElement("div")
                for (const [question, resp] of Object.entries(res)){
                    // console.log(question)
                    // console.log(resp)

                    resDiv.innerHTML += counter + ". " + question + "<br>"
                    const cls = ['container', 'p-3', 'text-light', 'h6']
                    resDiv.classList.add(...cls)

                    const correct = resp['correct_answer']
                    const answered = resp['answered']

                    if (correct == answered){
                        resDiv.classList.add('bg-success')
                        resDiv.innerHTML += `Answered : ${answered}`
                    } else {
                        resDiv.classList.add('bg-danger')
                        resDiv.innerHTML += `Answered : ${answered}`
                        resDiv.innerHTML += `, Correct : ${correct}`
                    }
                }

                counter += 1

                // const body = document.getElementsByTagName('BODY')[0]
                resultBox.append(resDiv)
                var timeDiff = endTime - startTime;
                timeDiff/=1000;
                var seconds = Math.round(timeDiff)
                console.log("Time taken : " + seconds)
                timeBox.innerHTML = `Time taken to complete the quiz is ${seconds} seconds`
                replaysBox.innerHTML = `Average number of replays per question is 0.8`
            })
        },
        error: function(error){
            console.log(error)
        }
    })
}

quizForm.addEventListener('submit', e => {
    e.preventDefault()
    endTime = new Date()
    sendData()
})
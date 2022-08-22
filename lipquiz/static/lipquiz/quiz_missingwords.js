console.log('hello world quiz')

const url = window.location.href
const quizBox = document.getElementById('quiz-box')
const quizForm = document.getElementById('quiz-form')
const scoreBox = document.getElementById('score-box')
const resultBox = document.getElementById('result-box')
const timeBox = document.getElementById('time-box')
const replaysBox = document.getElementById('replays-box')
var videoViews = 0

// record the time taken on the quiz 
const activateTimer = () => {
    startTime = new Date();
}

// loads the video quiz that was selected
$.ajax({
    type: 'GET',
    url: `${url}data/`,
    success: function(response){
        var counter = 1
        response.forEach(element => {
            quizBox.innerHTML += `
                <hr>
                <div class="mb-2">
                    <b>${counter}. ${element.question}</b>
                </div>

                <div class="mb-2">
                    <video width="460" controls muted>
                        <source src="/media/${element.video_path}" type="video/mp4">
                    </video>
                </div>
            `

            var content = ``
            content += `<div class="ans_wrapper">`
            
            content += `
                    <input autocomplete="false" type="text" class="ans" id="${element.question}" name="${element.video_path}" placeholder="Your answer" value="">
                    <div id="correct-${counter}" class="correct mwis-correct not-visible"></div>
            `
            content += `</div>`

            quizBox.innerHTML += content
            // quizBox.innerHTML += `</div>`

            counter += 1
        })

        // start the time after everything is successfully loaded 
        activateTimer()
        // countViews()
    },
    error: function(error){
        console.log(error)
    }
})

const csrfToken = document.getElementsByName('csrfmiddlewaretoken')

// Called at the submit of the form
const sendData = () => {
    const data = {}
    data['csrfmiddlewaretoken'] = csrfToken[0].value
    const elements = [...document.getElementsByClassName("ans")]

    elements.forEach(el => {
        // Get the value entered in the textbox for each text box question
        data[el.name] = el.value
    })

    $.ajax({
        type: 'POST',
        url: `${url}save/`,
        data: data,
        success: function(response){
            console.log(response)

            scoreBox.innerHTML = `Your score is ${response.score}%.`

            // Hide the form after the quiz is submitted and display the results
            const results = response.results
            console.log(results)
            // quizForm.classList.add('not-visible')

            const tryBtn = document.getElementById('try-again-btn')
            tryBtn.classList.remove('not-visible')

            var texts = document.getElementsByTagName('input');
            for (var i=0, iLen=texts.length; i<iLen; i++) {
                texts[i].disabled = true;
            } 

            var counter = 1
            results.forEach(res => {
                const resDiv = document.createElement("div")
                for (const [question, resp] of Object.entries(res)){
                    // console.log(question)
                    // console.log(resp)
                    // console.log('*****')

                    // resDiv.innerHTML += question
                    // const cls = ['container', 'p-3', 'text-light', 'h3']
                    // resDiv.classList.add(...cls)

                    // if (resp == 'not answered'){
                    //     resDiv.innerHTML += '-not answered'
                    //     resDiv.classList.add('bg-danger')
                    // }

                    const correct = resp['correct_answer']
                    const answered = resp['answered']


                    var label = question
                    var cl = "answered-wrong"
                    
                    if (correct == answered) {
                        cl = "answered-correct"
                        document.getElementById(label).classList.add('answered-correct')
                    }
                    else {
                        document.getElementById(label).classList.add('answered-wrong')

                        var correctDiv = document.getElementById('correct-'+counter)
                        correctDiv.innerHTML = correct
                        correctDiv.classList.remove('not-visible')
                    }

                    resDiv.innerHTML += `<div class="single-result">
                        <div class="single-result-blocks ans-num">${counter}</div> 
                        <div class="single-result-blocks ${cl}">
                        Answered: ${answered}</div>
                        <div class="single-result-blocks correct">Correct: ${correct}</div></div>`

                }
                counter += 1

                resultBox.append(resDiv)

                var timeDiff = endTime - startTime;
                timeDiff/=1000;
                var seconds = Math.round(timeDiff)
                console.log("Time taken : " + seconds)
                timeBox.innerHTML = `Time taken to complete the quiz is ${seconds} seconds`
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
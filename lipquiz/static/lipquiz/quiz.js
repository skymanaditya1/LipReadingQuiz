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

// Count the number of times videos have been played on the quiz
// const countViews = () => {
//     var v = document.getElementsByTagName("video")[0];
//     v.addEventListener("ended", function() { 
//         videoViews += 1;
//         alert(`Video has been viewed! ${videoViews}`); 
//     }, true);
// }

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
                    <video width="460" controls muted>
                        <source src="/media/${element.video_path}" type="video/mp4">
                    </video>
                </div>
            `

            var content = ``
            content += `<div class="ans_wrapper">`
            element.answer.forEach(choice => {
                content += `
                    <div class="ans_classes ans_single">
                        <input type="radio" class="ans" id="${element.video_path}-${choice}" name="${element.video_path}" value="${choice}" >
                        <label id="${counter}-${choice}" for="${element.video_path}-${choice}">${choice}</label>
                    </div>
                `
            });
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
            console.log(`Video views : ${videoViews}`)
            var counter = 1
            scoreBox.innerHTML = `Your score is ${response.score}%.`
            const results = response.results 
            // quizForm.classList.add('not-visible')

            const submitBtn = document.getElementById('submit-quiz-btn-id')
            submitBtn.classList.add('not-visible')

            const tryBtn = document.getElementById('try-again-btn')
            tryBtn.classList.remove('not-visible')

            var radios = document.getElementsByTagName('input');
            for (var i=0, iLen=radios.length; i<iLen; i++) {
                radios[i].disabled = true;
            } 

            var questions = document.getElementsByClassName('ans_classes');
            for (var i=0, iLen=questions.length; i<iLen; i++) {
                questions[i].classList.remove('ans_single')
                questions[i].classList.add('ans_single_submitted')
            }

            results.forEach(res => {
                const resDiv = document.createElement("div")
                for (const [question, resp] of Object.entries(res)){
                    // console.log(question)
                    // console.log(resp)

                    // resDiv.innerHTML += counter + ". " + question + "<br>"
                    // const cls = ['container', 'p-3', 'text-light', 'h6']
                    // resDiv.classList.add(...cls)

                    const correct = resp['correct_answer']
                    const answered = resp['answered']

                    
                    var label = counter+'-'+correct
                    var cl = "answered-wrong"
                    
                    if (correct == answered) {
                        cl = "answered-correct"
                        document.getElementById(label).classList.add('answered-correct')
                    }
                    else {
                        document.getElementById(label).classList.add('correct')
                    }


                    resDiv.innerHTML += `<div class="single-result">
                        <div class="single-result-blocks ans-num">${counter}</div> 
                        <div class="single-result-blocks ${cl}">
                        Answered: ${answered}</div>
                        <div class="single-result-blocks correct">Correct: ${correct}</div></div>`

                    // if (correct == answered){
                    //     resDiv.classList.add('bg-success')
                    //     resDiv.innerHTML += `Answered : ${answered}`
                    // } else {
                    //     resDiv.classList.add('bg-danger')
                    //     resDiv.innerHTML += `Answered : ${answered}`
                    //     resDiv.innerHTML += `, Correct : ${correct}`
                    // }
                }

                counter += 1

                // const body = document.getElementsByTagName('BODY')[0]
                resultBox.append(resDiv)
                var timeDiff = endTime - startTime;
                timeDiff/=1000;
                var seconds = Math.round(timeDiff)
                console.log("Time taken : " + seconds)
                timeBox.innerHTML = `Time taken to complete the quiz is ${seconds} seconds`
                // replaysBox.innerHTML = `Average number of replays per question is 0.8`
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
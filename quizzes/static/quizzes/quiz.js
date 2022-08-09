console.log('hello world quiz')
const url = window.location.href
const quiz_box = document.getElementById('quiz-box')
const score_box = document.getElementById('score-box')
const result_box = document.getElementById('result-box')
const timer_box = document.getElementById('timer-box')

const activateTimer = (time) => {
    console.log(time)

    if (time.toString().length < 2){
        timer_box.innerHTML = `<b>0${time}:00</b>`
    }
    else{
        timer_box.innerHTML = `<b>${time}:00</b>`
    }
    
    let seconds = 60 
    let minutes = time - 1
    let displaySeconds
    let displayMinutes

    const timer = setInterval(()=>{
        seconds -= 1
        if (seconds < 0){
            seconds = 59
            minutes --          
        }

        if (minutes.toString().length < 2){
            displayMinutes = "0" + minutes
        }
        else{
            displayMinutes = minutes
        }

        if (seconds.toString().length < 2){
            displaySeconds = "0" + seconds
        }
        else{
            displaySeconds = seconds
        }

        if (minutes === 0 && seconds === 0){
            timer.innerHTML = "00:00"
            setTimeout(()=>{
                console.log("Time up!")
                alert("Time up!")
                clearInterval(timer)
                sendData()    
            }, 500)
        }

        timer_box.innerHTML = `<b>${displayMinutes}:${displaySeconds}</b>`

    }, 1000)
}

$.ajax({
    type: 'GET',
    url: `${url}data`,
    success: function(response){
        console.log(response)
        data = response.data
        // iterate through all data items 
        data.forEach(element => {
            for (const [question, answers] of Object.entries(element)){
                quiz_box.innerHTML += `
                    <hr>
                    <div class="mb-2">
                        <b>${question}</b>
                    </div>
                `
                quizBox.innerHTML += `<div class="questions_wrapper">`
                answers.forEach(answer => {
                    quiz_box.innerHTML += `
                        <div>
                            <input type="radio" class="ans" id="${question}-${answer}" name="${question}" value="${answer}">
                            <label for="${question}">${answer}</label>
                        </div>
                    `
                })
                quizBox.innerHTML += `</div>`
            }
        });

        // If everything was successfully loaded, start the timer
        activateTimer(response.time)
    },
    error: function(error){
        console.log(error)
    }
})

const quizForm = document.getElementById('quiz-form')
const csrfToken = document.getElementsByName('csrfmiddlewaretoken')

const sendData = () => {
    const elements = [...document.getElementsByClassName('ans')]
    const data = {}
    data['csrfmiddlewaretoken'] = csrfToken[0].value
    elements.forEach(el => {
        // check if the radio button has been checked for that (question, answer) pair
        if (el.checked){
            data[el.name] = el.value;
        } else {
            if (!data[el.name]) {
                data[el.name] = null;
            }
        }
    })

    // make the ajax post request with the data 
    $.ajax({
        type: 'POST',
        url: `${url}save/`,
        data: data,
        success: function(response){
            score_box.innerHTML = `${response.passed ? 'Congratulations!' : 'Oops...'} Your score is ${response.score.toFixed(2)}%`
            const results = response.results 
            console.log(results)
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
                result_box.append(resDiv)
            })  
        },
        error: function(error){
            console.log(error)
        }
    })
}

quizForm.addEventListener('submit', e => {
    e.preventDefault()
    
    sendData()
})
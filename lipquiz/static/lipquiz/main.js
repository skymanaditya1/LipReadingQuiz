console.log("Inside the main.js file")

// register the onclick listeners for all the buttons 
const quizButtons = [...document.getElementsByClassName("start-quiz-button")]
const modalBody = document.getElementById("model-body-confirm")
const startButton = document.getElementById("start-button")
url = window.location.href 

// Grab all the information that needs to be displayed
quizButtons.forEach(quizButton => quizButton.addEventListener('click', () => {
    const name = quizButton.getAttribute("data-quiz")
    const pk = quizButton.getAttribute("data-pk")
    const questions = quizButton.getAttribute("data-questions")
    const description = quizButton.getAttribute("data-description")
    const difficulty = quizButton.getAttribute("data-difficulty")
    const quiz_type = quizButton.getAttribute("data-quiz-type")
    console.log(name)
    console.log(pk)

    modalBody.innerHTML = `
    <div class="h5 mb-3">Are you sure you want to begin "<b>${name}</b>"?</div>
    <div class="text-muted">
        <ul>
            <li>Description: <b>${description}</b></li>
            <li>Questions : <b>${questions}</b></li>        
            <li>Difficulty: <b>${difficulty}</b></li>
            <li>Quiz Type: <b>${quiz_type}</b></li>
        <ul>
    </div>
    `
    startButton.addEventListener('click', () => {
        window.location.href = url + pk
    })
}))
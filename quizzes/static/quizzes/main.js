console.log("hello world")

const modalBtns = [...document.getElementsByClassName("modal-button")]
const modalBody = document.getElementById("model-body-confirm")
const startButton = document.getElementById("start-button")
url = window.location.href

// modalBtns is a collection of modalBtn, for each modalBtn register an onclicklistener
modalBtns.forEach(modalBtn => modalBtn.addEventListener('click', () => {
    const pk = modalBtn.getAttribute("data-pk")
    const name = modalBtn.getAttribute("data-quiz")
    const questions = modalBtn.getAttribute("data-questions")
    const difficulty = modalBtn.getAttribute("data-difficulty")
    const time = modalBtn.getAttribute("data-time")
    const required_score = modalBtn.getAttribute("data-pass") 

    modalBody.innerHTML = `
        <div class="h5 mb-3">Are you sure you want to begin "<b>${name}</b>"?</div>
        <div class="text-muted">
            <ul>
                <li>Questions : <b>${questions}</b></li>
                <li>Difficulty: <b>${difficulty}</b></li>
                <li>Time to complete: <b>${time} mins</b></li>
                <li>Score required: <b>${required_score}%</b></li>
            <ul>
        </div>
    `

    // On button click, this takes us to the quiz with the pk specified
    startButton.addEventListener('click', () => {
        window.location.href = url + pk
    })
}))
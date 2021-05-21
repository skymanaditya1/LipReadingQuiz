console.log("Inside the main.js file")

// register the onclick listeners for all the buttons 
const quizButtons = [...document.getElementsByClassName("start-quiz-button")]
url = window.location.href 

quizButtons.forEach(quizButton => quizButton.addEventListener('click', () => {
    const name = quizButton.getAttribute("data-quiz")
    const pk = quizButton.getAttribute("data-pk")
    console.log(name)
    console.log(pk)
    window.location.href = url + pk
}))
let myForm = document.querySelector('#form')
console.log(myForm)
let budget = document.querySelector('#budgetslider')
let calories = document.querySelector('#calorieslider')
let submitButton = document.querySelector('#submit')

myForm.addEventListener('submit', submitBudgetAndCalories)

function submitBudgetAndCalories(e) {
    e.preventDefault()
    if (budget.value == 0 || calories.value == 0) {
        // submitButton.disabled = true
        alert("Please enter some values! UTM doesn't offer free food and food comes with calories :D")
    }
    
    console.log(budget.value,calories.value)
}

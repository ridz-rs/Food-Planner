const myForm = document.querySelector('.form-horizontal')
console.log(myForm)
const budget = document.querySelector('#budget')
const calories = document.querySelector('#calorie')
myForm.addEventListener('submit', submitBudgetAndCalories)

function submitBudgetAndCalories(e) {
    e.preventDefault()
    console.log(budget.value,calories.value)
}
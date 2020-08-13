
document.addEventListener('DOMContentLoaded', () => {
    document.querySelector('#form').onsubmit = () => {
        const request = new XMLHttpRequest();
        const calorie = document.querySelector('#calorieslider').value
        const price = document.querySelector('#budgetslider').value
        request.open('POST', '/food')
        request.onload = () => {
            const plans = JSON.parse(request.responseText)
            const plan1 = plans.plan1
            console.log(plans, plan1)
            var array = new Array()
            array = plan1[0]
            // for(let i=0; i<plan1[0].length;i++){
            //     console.log(plan1[0][i], plan1[1][i])
            // }
            localStorage.setItem('plans')
            localStorage.setItem('plans', plans)
            location.href = '/food'
        }
        const data = new FormData();
        data.append('calorie', calorie);
        data.append('price', price);

        request.send(data);
        return false
    }
})
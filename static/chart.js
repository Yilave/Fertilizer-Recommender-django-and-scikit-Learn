const form = document.querySelector('#chart-type-form')
const url = window.location.href

const csrf = document.getElementsByName('csrfmiddlewaretoken')[0].value;
const chartType = document.getElementsByTagName('Select')[0].value

// console.log(csrf);
// console.log(chartType);
// data = {
//     'csrfmiddlewaretoken': csrf,
//     'chart-type': chartType
// }
// form.addEventListener('submit', (e) => {
//     e.preventDefault()
//     // console.log('submitted');
//     $.ajax({
//         url: `${url}`,
//         type: 'POST',
//         data: data,
//         dataType: 'json',
//         success: (jsonResponse) => {
//             console.log(jsonResponse);
//         }
//     })
// })





// Charts JS

const ctx = document.getElementById('myChart')
$.ajax({
    url: `${url}chart/`,
    type: 'GET',
    dataType: 'json',
    success: (jsonResponse) => {
        console.log(jsonResponse);
        const type = jsonResponse.type
        const labels = jsonResponse.labels
        const data = jsonResponse.data
        const recommedations = jsonResponse.recommedations


        new Chart(ctx, {
            type: type,
            data: {
                labels: labels,
                datasets: [{
                    label: recommedations,
                    data: data,
                    borderWidth: 1
                }]
            },
            options: {
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            }
        });

    },
    error: (error) => {
        console.log('Error', error);
    }

})
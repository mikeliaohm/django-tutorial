const btn2 = document.getElementById("loadChart-btn");
var ctx = document.getElementById('myChart').getContext('2d');

btn2.onclick = (e) => {

    e.preventDefault();
    let employee_id = 'EM001';
    const url = `/mssql/attendance/?employee_id=${employee_id}`;
  
    console.log(url);
  
    buildAttendanceChart(url);
}

async function buildAttendanceChart(url) {

    const rawData = await $.ajax({
        dataType: "json",
        url: url
    });

    console.log(rawData);

    const data = JSON.parse(rawData);
    console.log(data);

    var myChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: data.month,
            datasets: [{
                label: 'Days Of Attendance',
                data: data.attendance,
                backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(255, 206, 86, 0.2)',
                    'rgba(75, 192, 192, 0.2)',
                    'rgba(153, 102, 255, 0.2)',
                    'rgba(255, 159, 64, 0.2)'
                ],
                borderColor: [
                    'rgba(255, 99, 132, 1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)',
                    'rgba(153, 102, 255, 1)',
                    'rgba(255, 159, 64, 1)'
                ],
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true
                    }
                }]
            }
        }
    });
}

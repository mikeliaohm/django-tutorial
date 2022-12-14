/* 
    loadSalary.js
    --------------

    定義loadSalary-btn button被點擊，所需要的動作。
    先從api取得salary json data，再來生成salary dom
*/

const btn = document.getElementById("loadSalary-btn");
const salaryContainer = document.getElementById("salaryContainer");

btn.onclick = (e) => {
    const employee_id = document.getElementById("employeeSelected").value;
    const month = document.getElementById("monthSelected").value;

    e.preventDefault();
    const url = `/sqlserver/salary/?employee_id=${employee_id}&month=${month}`;
    console.log('fetching URL: ' + url);

    loadJson(url);
}

async function loadJson(url) {
    const rawData = await $.ajax({
        dataType: "json",
        url: url
    });

    console.log(rawData);

    const data = JSON.parse(rawData);
    salaryContainer.innerHTML = "";
    buildBody(data);
}

function buildBody(data) {
    
    const salaryData = data[0].fields;
    const month = document.createElement("p");
    month.textContent = '計薪月份 (Month): ' + salaryData.month;

    const base = document.createElement("p");
    base.textContent = '月薪 (Base Salary): ' + salaryData.base_salary;

    const attendence = document.createElement("p");
    attendence.textContent = '出勤天數 (Attendence): ' + salaryData.days_of_attendance;

    const payment = document.createElement("p");
    payment.textContent = '實付金額 (Payment): ' + salaryData.salary_payment;

    const taxableIncome = document.createElement("p");
    taxableIncome.textContent = '課稅金額 (Taxable Income): ' + salaryData.taxable_amount;

    console.log('attendance: ' + salaryData.days_of_attendence);

    salaryContainer.appendChild(month);
    salaryContainer.appendChild(base);
    salaryContainer.appendChild(attendence);
    salaryContainer.appendChild(payment);
    salaryContainer.appendChild(taxableIncome);
}

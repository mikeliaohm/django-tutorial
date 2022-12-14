# 
# test.py
# ----------------
# by Griffon Development Co., Ltd
#
# Unit tests

import json

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from sqlserver.models import Employee, Salary

# Create your tests here.
class TestEmployeeDetailView(TestCase):

    databases = '__all__'

    def setUp(self):
        """
        database新增預設資料
        """

        User = get_user_model()
        # create user
        User.objects.create_user(username='test1', password='test1')

    def test_is_correct_template(self):
        """
        測試是否導向正確地的template
        """

        self.client.login(username='test1', password='test1')
        response = self.client.get(reverse('sqlserver:employee_detail'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'sqlserver/employee_detail.html')
    
    def test_no_authentication_redirect_to_login_page(self):
        """
        測試無權限者進入頁面，將導向登入頁面
        """

        response = self.client.get(reverse('sqlserver:employee_detail'))
        self.assertEqual(response.status_code, 302)

class TestSalaryView(TestCase):

    databases = '__all__'

    def setUp(self):
        """
        database新增預設資料
        """

        User = get_user_model()
        User.objects.create_user(username='test1', password='test1')

        self.test_employee_1 = Employee.objects.get_or_create(
            employee_id='EM001',
            employee_name='test_name',
            arrival_date='2022-1-1',
            salary_type=1,
            base_salary=30000)[0]

        self.test_salary_1 = Salary.objects.get_or_create(
            employee_id='EM001',
            month='202201',
            days_of_attendance=22,
            base_salary=30000,
            salary_payment=30000)[0]

        self.url = reverse('sqlserver:salary')

    def test_salary_view_get_data(self):
        """
        測試json response view回傳的資料是否與setUp的資料一致
        """

        self.client.login(username='test1', password='test1')
        employee_id = self.test_employee_1.employee_id
        month = self.test_salary_1.month

        response = self.client.get(
            f'{self.url}?employee_id={employee_id}&month={month}')

        data = json.loads(response.json())

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data[0]['fields']['employee_id'], employee_id)
        self.assertEqual(
            int(data[0]['fields']['base_salary']), 
            self.test_salary_1.base_salary)

    def test_no_authentication_redirect_to_login_page(self):
        """
        測試無權限者進入頁面，將導向登入頁面
        """

        employee_id = self.test_employee_1.employee_id
        month = self.test_salary_1.month

        response = self.client.get(
            f'{self.url}?employee_id={employee_id}&month={month}')
        self.assertEqual(response.status_code, 302)

class TestEmployeeManager(TestCase):

    databases = '__all__'

    def setUp(self):
        """
        database新增預設資料
        """

        self.test_employee_1 = Employee.objects.get_or_create(
            employee_id='EM001',
            employee_name='test_name',
            arrival_date='2022-1-1',
            salary_type=1,
            base_salary=30000)[0]

    def test_single_employee_data_get_employee(self):
        """
        測試manager method single_employee_data是否回傳正確的資料
        """

        single_employee_data = \
            Employee.objects.single_employee_data(self.test_employee_1.employee_id)
        
        self.assertEqual(
            single_employee_data.employee_id, self.test_employee_1.employee_id)

    def test_single_employee_data_with_invalid_employee_id(self):
        """
        測試manager method single_employee_data沒有輸入employee_id時，回傳None
        """

        single_employee_data = \
            Employee.objects.single_employee_data('test')

        self.assertEqual(single_employee_data, None)

class TestSalaryManager(TestCase):

    databases = '__all__'

    def setUp(self):
        """
        database新增預設資料
        """

        self.test_salary_1 = Salary.objects.get_or_create(
            employee_id='EM001',
            month='202201',
            days_of_attendance=22,
            base_salary=30000,
            salary_payment=30000)[0]

        self.month_list = ['202202', '202203', '202204', '202205', '202206']
        self.attendance_list = [15, 16, 20, 21, 22]
        for month, attendance in zip(self.month_list, self.attendance_list):

            Salary.objects.get_or_create(
                employee_id='EM001',
                month=month,
                days_of_attendance=attendance,
                base_salary=30000,
                salary_payment=30000
            )

    def test_single_salary_data_get_salary(self):
        """
        測試manager method single_salary_data是否回傳正確的資料
        """

        single_salary_data = \
            Salary.objects.single_salary_data(
                self.test_salary_1.employee_id, self.test_salary_1.month)
        
        self.assertEqual(
            single_salary_data.employee_id, self.test_salary_1.employee_id)
        self.assertEqual(
            single_salary_data.base_salary, self.test_salary_1.base_salary)

    def test_single_salary_data_no_employee_id(self):
        """
        測試manager method single_salary_data沒有輸入employee_id時，回傳None
        """

        single_salary_data = \
            Salary.objects.single_salary_data(
                None, self.test_salary_1.month)
        
        self.assertEqual(single_salary_data, None)

    def test_single_salary_data_no_month(self):
        """
        測試manager method single_salary_data沒有輸入month時，回傳empty qs
        """

        single_salary_data = \
            Salary.objects.single_salary_data(
                self.test_salary_1.employee_id, None)
        
        self.assertEqual(single_salary_data, None)

    def test_latest_five_month_attendance_get_data(self):
        """
        測試manager method latest_five_month_attendance是否回傳正確的資料
        """

        latest_five_month_attendance = \
            Salary.objects.latest_five_month_attendance(
                self.test_salary_1.employee_id)
        
        month_list = latest_five_month_attendance['month']
        attendance_list = latest_five_month_attendance['attendance']
        
        for i, (month, attendance) in enumerate(zip(month_list, attendance_list)):
            i = i + 1
            self.assertEqual(month, self.month_list[-i])
            self.assertEqual(attendance, self.attendance_list[-i])

    def test_latest_five_month_attendance_no_employee_id(self):
        """
        測試manager method latest_five_month_attendance沒有輸入employee_id時，
        回傳empty qs
        """
        
        latest_five_month_attendance = \
            Salary.objects.latest_five_month_attendance(None)

        self.assertEqual(latest_five_month_attendance.exists(), False)

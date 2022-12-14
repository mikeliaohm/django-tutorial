# 
# managers.py
# ----------------
# by Griffon Development Co., Ltd
#
# A Manager is the interface through which database query operations are 
# provided to Django models. At least one Manager exists for every model 
# in a Django application. 
# https://docs.djangoproject.com/en/3.2/topics/db/managers/

from django.db import models
from django.core.exceptions import ObjectDoesNotExist

class EmployeeManager(models.Manager):

    def single_employee_data(self, employee_id=None):
        """
        Fetch a single employee data.

        :param employee_id: Employee ID string, e.g. EM001
        :return: an Employee object if there is a matching ID, or None
        """ 

        employee_data = None

        if employee_id:
            try:
                employee_data = self.get(employee_id=employee_id)
            except ObjectDoesNotExist:
                pass

        return employee_data

class SalaryManager(models.Manager):

    def single_salary_data(self, employee_id=None, month=None):
        """
        Fetch the salary data.

        :param employee_id: Employee ID string, e.g. EM001
        :param month: year + month string, e.g. 202208
        :return: a Salary object if there is a matching ID, or None
        """ 

        salary_data = None

        if employee_id and month:
            try:
                salary_data = self.get(employee_id=employee_id, month=month)
            except ObjectDoesNotExist:
                pass

        return salary_data

    def latest_five_month_attendance(self, employee_id=None):
        """
        Fetch the lastest five month attendance data.

        :param employee_id: Employee ID string, e.g. EM001
        :param month: year + month string, e.g. 202208
        :return: data that lists months and attendance data (as a dictionary) if
                 there is a matching record, or emtpy queryset
        """ 

        attendance_data = self.none()
        if not employee_id:
            return attendance_data

        qs = self\
            .filter(employee_id=employee_id)\
            .order_by('-month')\
            .values_list('month', 'days_of_attendance')[0:5]

        month_list = []
        attendance_list = []

        for month, attendance in qs:
            month_list.append(month)
            attendance_list.append(float(attendance))

        return {'month': month_list, 'attendance': attendance_list}
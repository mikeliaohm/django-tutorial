# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

from .managers import EmployeeManager, SalaryManager


class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    employee_id = models.CharField(max_length=50)
    employee_name = models.CharField(max_length=50, blank=True, null=True)
    arrival_date = models.CharField(max_length=50, blank=True, null=True)
    salary_type = models.CharField(max_length=50, blank=True, null=True)
    base_salary = models.DecimalField(max_digits=18, decimal_places=0, blank=True, null=True)

    objects = EmployeeManager() # custom manager class

    class Meta:
        managed = False
        db_table = 'EMPLOYEE'

    # model instance getter employee name
    @property
    def name(self):
        return self.employee_name

    # model instance getter arrival date
    @property
    def start_date(self):
        return self.arrival_date

    # model instance getter salary type
    @property
    def salary_type_name(self):

        if self.salary_type == '1':
            return 'Monthly'
        elif self.salary_type == '2':
            return 'Daily'
        else:
            return 'Hourly'

class Salary(models.Model):
    id = models.AutoField(primary_key=True)
    employee_id = models.CharField(max_length=50)
    month = models.CharField(max_length=50, blank=True, null=True)
    days_of_attendance = models.DecimalField(max_digits=18, decimal_places=0, blank=True, null=True)
    days_of_leaves_deductible = models.DecimalField(max_digits=18, decimal_places=0, blank=True, null=True)
    base_salary = models.DecimalField(max_digits=18, decimal_places=0, blank=True, null=True)
    leaves_deductible_amount = models.DecimalField(max_digits=18, decimal_places=0, blank=True, null=True)
    health_insurance = models.DecimalField(max_digits=18, decimal_places=0, blank=True, null=True)
    labor_insurance = models.DecimalField(max_digits=18, decimal_places=0, blank=True, null=True)
    tax_deduction = models.DecimalField(max_digits=18, decimal_places=0, blank=True, null=True)
    salary_payment = models.DecimalField(max_digits=18, decimal_places=0, blank=True, null=True)
    taxable_amount = models.DecimalField(max_digits=18, decimal_places=0, blank=True, null=True)
    pension = models.DecimalField(max_digits=18, decimal_places=0, blank=True, null=True)
    supplementary_health_insurance = models.DecimalField(max_digits=18, decimal_places=0, blank=True, null=True)

    objects = SalaryManager() # custom manager class

    class Meta:
        managed = False
        db_table = 'SALARY'

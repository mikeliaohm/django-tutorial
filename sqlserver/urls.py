from django.urls import path

from . import views

app_name = "sqlserver"

urlpatterns = [
    # url info/ - EmployeeDetail class view
    path("info/", views.EmployeeDetail.as_view(), name="employee_detail"),

    # url salary/ salary_view function view
    path("salary/", views.salary_view, name="salary"),
]
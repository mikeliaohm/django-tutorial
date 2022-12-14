from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import JsonResponse
from django.views.generic import TemplateView

# Create your views here.
from .models import Employee, Salary

@method_decorator(login_required, name='dispatch')
class EmployeeDetail(TemplateView):
    """
    Shows the employee detail, requires login.
    """

    model = Employee
    template_name = "sqlserver/employee_detail.html"

    def get(self, request, *args, **kwargs):
        """
        Retrieve employee_id from request.GET to fetch an employee object and 
        populate the information in the html.

        :param employee_id: Employee ID, e.g. EM001
        returns: HttpResponse
        """

        context = self.get_context_data(**kwargs)

        employee_id = request.GET.get("employee_id")

        employee_data = \
            self.model.objects.single_employee_data(employee_id=employee_id)

        context.update({
            "employee_data": employee_data, "employee_id": employee_id})

        return self.render_to_response(context)

@login_required
def salary_view(request):
    """
    Salary API endpoint. Retrieve employee_id and month from request.GET to 
    fetch a salary object and return a JSON response.
    :param employee_id: employee ID, e.g. EM001
    :param month: year + month string, e.g. 202209
    :returns: JsonResponse
    """

    employee_id = request.GET.get("employee_id")
    month = request.GET.get("month")

    salary = \
        Salary.objects.single_salary_data(employee_id=employee_id, month=month)

    json_data = serializers.serialize('json', [salary])

    return JsonResponse(json_data, safe=False)
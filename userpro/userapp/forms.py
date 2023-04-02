from django import forms
from .models import Employee, Designation

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('name', 'email', 'address', 'photo', 'designation')

class DesignationForm(forms.ModelForm):
    class Meta:
        model = Designation
        fields = ('name',)

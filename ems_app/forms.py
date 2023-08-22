from django import forms

from ems_app.models import Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'style': 'max-width:300px',
                    'placeholder': 'Enter your first name..'
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'style': 'max-width:300px',
                    'placeholder': 'Enter your last name..'
                }
            ),
            'salary': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'style': 'max-width:300px',
                    'placeholder': 'Enter your salary..'
                }
            ),
            'age': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'style': 'max-width:300px',
                    'placeholder': 'Enter your Age..'
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'style': 'max-width:300px',
                    'placeholder': 'Enter your email..'
                }
            ),
        }

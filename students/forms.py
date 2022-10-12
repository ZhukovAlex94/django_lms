from django import forms

from django_filters import FilterSet

from .models import Student


class BaseStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
          # '__all__',
          'first_name',
          'last_name',
          'birthday',
          'email',
          'phone_number',
        ]

        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'})
        }

    # def clean(self):
    #     clean_data = super().clean()
    #     if 'first_name' in clean_data:
    #         clean_data['first_name'] = clean_data['first_name'].title()
    #     return clean_data

    def clean_birthday(self):
        value = self.cleaned_data.get('birthday')

        return value

    def clean_first_name(self):
        return self.cleaned_data['first_name'].title()

    def clean_last_name(self):
        return self.cleaned_data['last_name'].title()

    def clean_phone_number(self):
        value = self.cleaned_data['phone_number']
        return "".join(char for char in value if char in "0123456789-()")


class CreateStudentForm(BaseStudentForm):
    pass


class UpdateStudentForm(BaseStudentForm):
    class Meta(BaseStudentForm.Meta):
        fields = [
            # '__all__',
            'first_name',
            'last_name',
            'birthday',
        ]

        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'})
        }


class StudentFilterForm(FilterSet):
    class Meta:
        model = Student
        fields = {
            'first_name': ['exact', 'icontains'],
            'last_name': ['exact', 'startswith']
        }

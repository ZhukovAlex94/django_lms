from django import forms

from .models import Teacher


class CreateTeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = [
          # '__all__',
          'first_name',
          'last_name',
          'job',
          'birthday',
          'email',
          'phone_number',
        ]

        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'})
        }

    # def clean(self):

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


class UpdateTeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = [
            # '__all__',
            'first_name',
            'last_name',
            'birthday',
            'job',
            'phone_number',
        ]

        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'})
        }

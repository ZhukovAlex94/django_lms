from django import forms

from .models import Group


class UpdateGroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = [
            # '__all__',
            'group_name',
            'group_start_date',
            'group_description',
        ]

        widgets = {
            'group_start_date': forms.DateInput(attrs={'type': 'date'})
        }

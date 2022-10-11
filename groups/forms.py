from django import forms

from django_filters import FilterSet

from .models import Group


# class GroupBaseForm(forms.ModelForm):
#     class Meta:
#         model = Group
#         fields = [
#             'name',
#             'group_start_date',
#             'group_end_date',
#         ]
#
#         widgets = {
#             'group_start_date': forms.DateInput(attrs={'type': 'date'}),
#             'group_end_date': forms.DateInput(attrs={'type': 'date'}),
#         }


class CreateGroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = [
            'group_name',
            'group_start_date',
            'group_end_date',
            'group_description',
        ]

        widgets = {
            'group_start_date': forms.DateInput(attrs={'type': 'date'}),
            'group_end_date': forms.DateInput(attrs={'type': 'date'}),
        }


class UpdateGroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = [
            # '__all__',
            'group_name',
            'group_start_date',
            'group_end_date',
            'group_description',
        ]

        widgets = {
            'group_start_date': forms.DateInput(attrs={'type': 'date'}),
            'group_end_date': forms.DateInput(attrs={'type': 'date'}),
        }
        # exclude = [
        #     'group_start_date',
        # ]


class GroupFilterForm(FilterSet):
    class Meta:
        model = Group
        fields = {
            'group_name': ['exact', 'icontains'],
        }

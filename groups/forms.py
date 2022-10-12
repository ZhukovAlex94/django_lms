from django import forms

from django_filters import FilterSet

from .models import Group


class GroupBaseForm(forms.ModelForm):
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


class CreateGroupForm(GroupBaseForm):
    pass


class UpdateGroupForm(GroupBaseForm):
    class Meta(GroupBaseForm.Meta):
        exclude = [
            'group_start_date',
        ]


class GroupFilterForm(FilterSet):
    class Meta:
        model = Group
        fields = {
            'group_name': ['exact', 'icontains'],
        }

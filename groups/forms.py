from django import forms

from django_filters import FilterSet

from .models import Group


class GroupBaseForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = '__all__'

        widgets = {
            'group_start_date': forms.DateInput(attrs={'type': 'date'}),
            'group_end_date': forms.DateInput(attrs={'type': 'date'}),
        }


class CreateGroupForm(GroupBaseForm):
    # from students.models import Student
    # students = forms.ModelMultipleChoiceField(queryset=Student.objects.select_related('group'), required=False)
    # # students = forms.ModelMultipleChoiceField(queryset=Student.objects.filter(group__isnull=True), required=False)

    def __init__(self, *args, **kwargs):
        from students.models import Student
        super().__init__(*args, **kwargs)
        self.fields['students'] = forms.ModelMultipleChoiceField(
            queryset=Student.objects.select_related('group'),
            required=False
        )

    # def save(self, commit=True):
    #     group = super().save(commit)
    #     students = self.cleaned_data['students']
    #     for student in students:
    #         student.group = group
    #         student.save()

    class Meta(GroupBaseForm.Meta):
        exclude = [
            'headman'
        ]


class UpdateGroupForm(GroupBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['headman_field'] = forms.ChoiceField(
            choices=[(st.pk, f'{st.first_name} {st.last_name}') for st in self.instance.students.all()],
            label='Headman',
            required=False,
        )
        self.fields['headman_field'].choices.insert(0, (0, '------------'))

    class Meta(GroupBaseForm.Meta):
        exclude = [
            'group_start_date',
            'headman'
        ]


class GroupFilterForm(FilterSet):
    class Meta:
        model = Group
        fields = {
            'group_name': ['exact', 'icontains'],
        }

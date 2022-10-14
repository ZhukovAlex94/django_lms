from django import forms

from django_filters import FilterSet

from .models import Course


class CourseBaseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'


class CreateCourseForm(CourseBaseForm):
    pass


class UpdateCourseForm(CourseBaseForm):
    pass


class CourseFilterForm(FilterSet):
    class Meta:
        model = Course
        fields = {
            'course_name': ['exact', 'icontains'],
        }

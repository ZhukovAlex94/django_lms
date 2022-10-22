from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from .forms import CourseFilterForm, CreateCourseForm, UpdateCourseForm
from .models import Course


class ListCourseView(ListView):
    model = Course
    template_name = 'courses/list.html'

    def get_queryset(self):
        courses = Course.objects.all()
        filter_form = CourseFilterForm(data=self.request.GET, queryset=courses)

        return filter_form


class CreateCourseView(LoginRequiredMixin, CreateView):
    model = Course
    template_name = 'courses/create.html'
    success_url = reverse_lazy('courses:list')
    form_class = CreateCourseForm


class DetailCourseView(LoginRequiredMixin, DetailView):
    model = Course
    template_name = 'courses/detail.html'


class UpdateCourseView(LoginRequiredMixin, UpdateView):
    model = Course
    template_name = 'courses/update.html'
    form_class = UpdateCourseForm
    success_url = reverse_lazy('courses:list')


class DeleteCourseView(LoginRequiredMixin, DeleteView):
    model = Course
    template_name = 'courses/delete.html'
    success_url = reverse_lazy('courses:list')

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView

from .forms import CreateTeacherForm, TeacherFilterForm, UpdateTeacherForm
from .models import Teacher


def get_teachers(request):
    teachers = Teacher.objects.all()

    filter_form = TeacherFilterForm(data=request.GET, queryset=teachers)

    return render(
        request=request,
        template_name='teachers/list.html',
        context={
            'filter_form': filter_form
        }
    )


class CreateTeacherView(CreateView):
    model = Teacher
    template_name = 'teachers/create.html'
    success_url = reverse_lazy('teachers:list')
    form_class = CreateTeacherForm


class DetailTeacherView(DetailView):
    model = Teacher
    template_name = 'teachers/detail.html'


class UpdateTeacherView(UpdateView):
    model = Teacher
    template_name = 'teachers/update.html'
    success_url = reverse_lazy('teachers:list')
    form_class = UpdateTeacherForm


class DeleteTeacherView(DeleteView):
    model = Teacher
    template_name = 'teachers/delete.html'
    success_url = reverse_lazy('teachers:list')

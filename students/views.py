from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views.generic import UpdateView, ListView, DetailView, DeleteView, CreateView

# from core.views import CustomUpdateBaseView
from .forms import CreateStudentForm, StudentFilterForm, UpdateStudentForm
from .models import Student


def get_students(request):
    students = Student.objects.select_related('group')

    filter_form = StudentFilterForm(data=request.GET, queryset=students)

    return render(
        request=request,
        template_name='students/list.html',
        context={
            'filter_form': filter_form
        }
    )


# class ListStudentView(ListView):
#     model = Student
#     template_name = 'students/list.html'
#     context_object_name = ''


class DetailStudentView(DetailView):
    model = Student
    template_name = 'students/detail.html'


# def create_student(request):
#     if request.method == 'GET':
#         form = CreateStudentForm()
#     elif request.method == 'POST':
#         form = CreateStudentForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('students:list'))
#
#     return render(request, 'students/create.html', {'form': form})


class CreateStudentView(CreateView):
    model = Student
    template_name = 'students/create.html'
    success_url = reverse_lazy('students:list')
    fields = '__all__'


# def update_student(request, student_id):
#     student = get_object_or_404(Student, pk=student_id)
#
#     if request.method == 'GET':
#         form = UpdateStudentForm(instance=student)
#     elif request.method == 'POST':
#         form = UpdateStudentForm(request.POST, instance=student)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('students:list'))
#
#     form = UpdateStudentForm(instance=student)
#
#     return render(request, 'students/update.html', {'form': form})


# class CustomUpdateStudentView(CustomUpdateBaseView):
#     model = Student
#     form_class = UpdateStudentForm
#     success_url = 'students:list'
#     template_name = 'students/update.html'


class UpdateStudentView(UpdateView):
    model = Student
    form_class = UpdateStudentForm
    success_url = reverse_lazy('students:list')
    template_name = 'students/update.html'


class DeleteStudentView(DeleteView):
    model = Student
    template_name = 'students/delete.html'
    success_url = reverse_lazy('students:list')

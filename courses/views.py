from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView

from .forms import CourseFilterForm, CreateCourseForm, UpdateCourseForm
from .models import Course


def get_courses(request):
    courses = Course.objects.all()

    filter_form = CourseFilterForm(data=request.GET, queryset=courses)

    return render(
        request=request,
        template_name='courses/list.html',
        context={
            'filter_form': filter_form,
        }
    )


class CreateCourseView(CreateView):
    model = Course
    template_name = 'courses/create.html'
    success_url = reverse_lazy('courses:list')
    form_class = CreateCourseForm


class DetailCourseView(DetailView):
    model = Course
    template_name = 'courses/detail.html'


class UpdateCourseView(UpdateView):
    model = Course
    template_name = 'courses/update.html'
    form_class = UpdateCourseForm
    success_url = reverse_lazy('courses:list')


# def delete_course(request, course_id):
#     course = get_object_or_404(Course, pk=course_id)
#
#     if request.method == 'POST':
#         course.delete()
#         return HttpResponseRedirect(reverse('courses:list'))
#
#     return render(request, 'courses/delete.html', {'course': course})


class DeleteCourseView(DeleteView):
    model = Course
    template_name = 'courses/delete.html'
    success_url = reverse_lazy('courses:list')

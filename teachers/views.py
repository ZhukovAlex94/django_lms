from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.middleware.csrf import get_token
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt    # noqa

from webargs.djangoparser import use_args
from webargs.fields import Str

from .forms import UpdateTeacherForm
from .models import Teacher


# HttpRequest
def index(request):
    return HttpResponse('Welcome to LMS!')


@use_args(
    {
        'first_name': Str(required=False),
        'last_name': Str(required=False),
    },
    location='query'
)
def get_teachers(request, args):
    teachers = Teacher.objects.all()

    if len(args) and args.get('first_name') or args.get('last_name'):
        teachers = teachers.filter(
            Q(first_name=args.get('first_name', '')) | Q(last_name=args.get('last_name', ''))
        )

    return render(request=request,
                  template_name='teachers/list.html',
                  context={
                      'title': 'List of teachers',
                      'teachers': teachers,
                  }
                  )


def detail_teacher(request, teacher_id):
    teacher = Teacher.objects.get(pk=teacher_id)
    return render(request, 'teachers/detail.html', {'teacher': teacher})


def update_teacher(request, teacher_id):
    teacher = Teacher.objects.get(pk=teacher_id)

    if request.method == 'GET':
        form = UpdateTeacherForm(instance=teacher)
    elif request.method == 'POST':
        form = UpdateTeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/teachers/')

    token = get_token(request)
    html_form = f'''
        <form method="post">
            <input type="hidden" name="csrfmiddlewaretoken" value="{token}">
            <table>
                {form.as_table()}
            </table>
            <input type="submit" value="Submit">
        </form>
    '''

    return HttpResponse(html_form)

from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.middleware.csrf import get_token
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt    # noqa

from webargs.djangoparser import use_args
from webargs.fields import Str

from .forms import UpdateGroupForm
from .models import Group


@use_args(
    {
        'group_name': Str(required=False),
    },
    location='query'
)
def get_groups(request, args):
    groups = Group.objects.all()

    if len(args) and args.get('group_name'):
        groups = groups.filter(
            Q(group_name=args.get('group_name'))
        )

    return render(
        request=request,
        template_name='groups/list.html',
        context={
            'title': 'List of groups',
            'groups': groups,
        }
    )


def detail_group(request, group_id):
    group = Group.objects.get(pk=group_id)
    return render(request, 'groups/detail.html', {'group': group})


def update_group(request, group_id):
    group = Group.objects.get(pk=group_id)

    if request.method == 'GET':
        form = UpdateGroupForm(instance=group)
    elif request.method == 'POST':
        form = UpdateGroupForm(request.POST, instance=group)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/groups/')

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

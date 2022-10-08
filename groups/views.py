from django.db.models import Q
from django.http import HttpResponse    # noqa
from django.http import HttpResponseRedirect
from django.middleware.csrf import get_token    # noqa
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt  # noqa

from webargs.djangoparser import use_args
from webargs.fields import Str

from .forms import CreateGroupForm, UpdateGroupForm
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


def create_group(request):
    if request.method == 'GET':
        form = CreateGroupForm()
    elif request.method == 'POST':
        form = CreateGroupForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('groups:list'))

    return render(request, 'groups/create.html', {'form': form})


def detail_group(request, group_id):
    group = Group.objects.get(pk=group_id)
    return render(request, 'groups/detail.html', {'group': group})


def update_group(request, group_id):
    group = get_object_or_404(Group, pk=group_id)

    if request.method == 'GET':
        form = UpdateGroupForm(instance=group)
    elif request.method == 'POST':
        form = UpdateGroupForm(request.POST, instance=group)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('groups:list'))

    return render(request, 'groups/update.html', {'form': form})


def delete_group(request, group_id):
    group = get_object_or_404(Group, pk=group_id)

    if request.method == 'POST':
        group.delete()
        return HttpResponseRedirect(reverse('groups:list'))

    return render(request, 'groups/delete.html', {'group': group})

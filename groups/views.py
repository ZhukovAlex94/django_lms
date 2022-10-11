from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .forms import CreateGroupForm, GroupFilterForm, UpdateGroupForm
from .models import Group


def get_groups(request):
    groups = Group.objects.all()

    filter_form = GroupFilterForm(data=request.GET, queryset=groups)

    return render(
        request=request,
        template_name='groups/list.html',
        context={
            'filter_form': filter_form,
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

    return render(request, 'groups/update.html', {'form': form, 'group': group})


def delete_group(request, group_id):
    group = get_object_or_404(Group, pk=group_id)

    if request.method == 'POST':
        group.delete()
        return HttpResponseRedirect(reverse('groups:list'))

    return render(request, 'groups/delete.html', {'group': group})

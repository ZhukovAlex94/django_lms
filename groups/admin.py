from django.contrib import admin

from groups.models import Group

from rangefilter.filters import DateRangeFilter


class GroupAdmin(admin.ModelAdmin):
    list_display = ('group_name', 'group_description', 'group_start_date', )
    list_display_links = list_display
    list_filter = (('group_start_date', DateRangeFilter), 'group_name',)
    fieldsets = (
        ('Group info', {'fields': ('group_name',)}),
        ('Group dates', {'fields': ('group_start_date', 'group_end_date')}),
        ('Group description', {'fields': ('group_description',)}),
        ('Teachers and Headman', {'fields': ('teachers', 'headman')}),
    )


admin.site.register(Group, GroupAdmin)

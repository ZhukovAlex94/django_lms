from django.contrib import admin

from groups.models import Group

from rangefilter.filters import DateRangeFilter


class StudentInlineTable(admin.TabularInline):
    from students.models import Student
    model = Student
    fields = ('first_name', 'last_name', 'email')
    extra = 0
    readonly_fields = fields
    # show_change_link = True

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj):
        return False


class TeacherInlineTable(admin.TabularInline):
    model = Group.teachers.through
    fields = ('last_name', 'first_name', 'email', 'salary',)
    extra = 0
    readonly_fields = fields

    def first_name(self, obj):  # noqa
        return obj.teacher.first_name

    def last_name(self, obj):  # noqa
        return obj.teacher.last_name

    def email(self, obj):  # noqa
        return obj.teacher.email

    def salary(self, obj):  # noqa
        return obj.teacher.salary

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj):
        return False


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('group_name', 'group_start_date', 'group_start_date',)
    list_display_links = list_display
    list_filter = (('group_start_date', DateRangeFilter), 'group_name',)
    fieldsets = (
        ('Group info', {'fields': ('group_name',)}),
        ('Group dates', {'fields': ('group_start_date', 'group_end_date')}),
        ('Group description', {'fields': ('group_description',)}),
        ('Teachers and Headman', {'fields': ('headman',)}),
        ('Fixed dates', {'fields': ('create_datetime', 'update_datetime')}),
    )

    readonly_fields = ('create_datetime', 'update_datetime')

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj, change, **kwargs)
        form.base_fields['headman'].widget.can_add_related = False
        form.base_fields['headman'].widget.can_change_related = False
        form.base_fields['headman'].widget.can_delete_related = False
        form.base_fields['headman'].widget.can_view_related = False

        return form

    inlines = [StudentInlineTable, TeacherInlineTable, ]

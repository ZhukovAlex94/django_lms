from django.contrib import admin

from courses.models import Course


class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_name', 'duration', 'price')
    list_display_links = list_display
    list_per_page = 15
    list_filter = ('course_name',)
    fieldsets = (
        ('Course information', {'fields': ('course_name',)}),
        ('Course description', {'fields': ('duration', 'description', 'price')}),
        ('Relevant group', {'fields': ('group',)}),
    )


admin.site.register(Course, CourseAdmin)

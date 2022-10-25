from django.contrib import admin

from teachers.models import Teacher

from datetime import date


class SalaryListFilter(admin.SimpleListFilter):
    title = 'salary filter'
    parameter_name = 'salary_filter'

    def lookups(self, request, model_admin):

        return [
            ('< 10000', '< less than 10000'),
        ] + [
            (f'{i}0000 - {i+1}0000', f'{i}0000 - {i+1}0000') for i in range(1, 10)
        ] + [
            ('> 100000', '> more than 100000')
        ]

    def queryset(self, request, queryset):
        value = self.value().split() if self.value() is not None else None
        match value:
            case ['<', amount]:
                return Teacher.objects.filter(salary__lt=amount)
            case ['>', amount]:
                return Teacher.objects.filter(salary__gte=amount)
            case [gte, '-', lt]:
                return Teacher.objects.filter(salary__gte=gte, salary__lt=lt)
            case _:
                return Teacher.objects.all()


class AgeListFilter(admin.SimpleListFilter):
    title = 'age filter'
    parameter_name = 'age_filter'

    def lookups(self, request, model_admin):
        return [
            ('< 18', '< less than 18 years old'),
        ] + [
            ('> 18', '> more than 18 years old'),
        ]

    def queryset(self, request, queryset):
        today = date.today()
        value = self.value().split() if self.value() is not None else None
        match value:
            case ['<' | '>' as op, age] if age.isdigit():
                min_date_required = date(today.year - int(age), today.month, today.day)
                if op == '<':
                    return Teacher.objects.filter(birthday__lt=min_date_required)
                else:
                    return Teacher.objects.filter(birthday__gte=min_date_required)
            case _:
                return Teacher.objects.all()


class TeacherAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'salary')
    list_display_links = list_display
    list_per_page = 15
    list_filter = (SalaryListFilter, AgeListFilter)
    fieldsets = (
        ('Personal information', {'fields': ('last_name', 'first_name')}),
        ('DOB', {'fields': ('birthday', 'age')}),
        ('Contacts', {'fields': ('email', 'phone_number')}),
        ('Salary', {'fields': ('salary',)})
    )

    def age(self, instance):
        return f'{instance.get_age()} y.o.'

    readonly_fields = ('age',)
    age.short_description = 'age'


admin.site.register(Teacher, TeacherAdmin)

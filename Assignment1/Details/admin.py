from django.contrib import admin
from .models import Student,Department


# Register your models here.


class StudentAdmin(admin.ModelAdmin):
    list_display = ('firstname','lastname','dob','department_name','course_name')


admin.site.register(Student,StudentAdmin)
admin.site.register(Department)

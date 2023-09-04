from django.contrib import admin
from .models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name',)

admin.site.register(Student, StudentAdmin)

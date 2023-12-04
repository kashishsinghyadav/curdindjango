from django.contrib import admin
from .models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display=('id','name','st_id','city')

admin.site.register(Student,StudentAdmin)

# Register your models here.

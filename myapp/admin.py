from django.contrib import admin
from myapp.models import Resume

# Register your models here.

class ResumeAdmin(admin.ModelAdmin):
    list_display=('name','dob','gen','locality','city','code','state','mob','email','jobloc','img','doc')

admin.site.register(Resume,ResumeAdmin)

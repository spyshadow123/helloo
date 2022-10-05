from django.contrib import admin

# Register your models here.
from resume.models import My
@admin.register(My)
class MyAdmin(admin.ModelAdmin):
    list_display=['id','name','email','mobile','message']
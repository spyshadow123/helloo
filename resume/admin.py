from django.contrib import admin

from resume.models import My,MediaFile,Style_JS
@admin.register(My)
class MyAdmin(admin.ModelAdmin):
    list_display=['id','name','email','mobile','message']
@admin.register(MediaFile)
class MediaFileAdmin(admin.ModelAdmin):
    list_display=['id','file']
@admin.register(Style_JS)
class StyleAdmin(admin.ModelAdmin):
    list_display=['id','style','js']
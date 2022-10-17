from django.db import models

# Create your models here.
class My(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    mobile=models.CharField(max_length=100)
    message=models.CharField(max_length=100)
    

    class Meta:
        ordering=['id']
        
class MediaFile(models.Model):
    file=models.FileField( )
    class Meta:
        ordering=['id']
class Style_JS(models.Model):
    style=models.TextField()
    js=models.TextField()
    class Meta:
        ordering=['id']

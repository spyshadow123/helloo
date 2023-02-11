from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from resume.views import home,about,contact,register,login,logout,secure,data,skill

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('about',about,name='about'),
    path('contact',contact,name='contact'),
    path('register',register,name='register'),
    path('login',login,name='login'),
    path('logout',logout,name='logout'),
    path('secure',secure,name='secure'),
    path('data',data,name='data'),
    path('skill',skill,name='skill'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

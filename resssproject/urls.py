from django.contrib import admin
from django.urls import path
from resss import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.submit_form, name='submit_form'),
    path('data/', views.view_data, name='view_data'),
]

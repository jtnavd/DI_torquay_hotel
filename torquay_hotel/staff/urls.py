from django.contrib import admin
from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.staff_login, name='Login'),
    path('register',views.register_request, name='register'),
    path('staff/list', views.StaffListView.as_view(), name='staff_list')
]
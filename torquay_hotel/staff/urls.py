from django.contrib import admin
from . import Views

urlpatterns = [
    path('staff_login.html', views.index, name='index')
    path('staff/list', views.StaffListView.as_view(), name='staff_list')
]
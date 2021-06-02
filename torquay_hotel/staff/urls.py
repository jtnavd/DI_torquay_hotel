from django.contrib import admin
from . import Views

urlpatterns = [
    path('', views.index, name='index')
    path('staff/list', views.StaffListView.as_view(), name='staff_list')
]
from django.shortcuts import render
from django.views import Views
from .models import Staff

def render(request):
    return render(request, 'index.html')


class StaffListView(generic.ListView):
    model = Staff
    template_name = 'staff_list'
    context_object_name = 'staffs'
    


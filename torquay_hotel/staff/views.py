from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib.auth.models import login
from django.contrib import messages
from django.views import generic
from .models import Staff


def index(request):
    return render(request, 'index.html')


class StaffListView(generic.ListView):
    model = Staff
    template_name = 'staff_list'
    context_object_name = 'staffs'

def register_request(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request.user)
            messages.success(request,'Registration Successful!')
            return redirect('main:login')
        messages.error(request,'Registration Error. Invalid Information')
    form = NewUserForm
    return render(request=request, template_name='main/register.html', context={'register_form':form})
    


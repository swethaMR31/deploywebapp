from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import  login_required
from django.contrib import messages
from .forms import Registerform

from django.views.generic.edit import CreateView, UpdateView,DeleteView,FormView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


def index(request):
    return render(request, "Administration/home.html")
#def login(request):
 #   return render(request, "registration/login.html")

def logout(request):
    return render(request, "Administration/logout.html")
@login_required
def main(request):
    return render(request, "Administration/index.html")


'''@login_required
def candidate(request):
    return render(request, "Administration/player_form.html")'''


def register(request):
    if request.method=="POST":
        form=Registerform(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            messages.success(request,f'Welcome {username} your account is created successfully')
            return redirect('login')
            #user=authenticate(username=username,password=password)
            #login(request,user)
            #return redirect('login')
    else:
        form=Registerform()
    context={'form':form}
    return render(request,'registration/register.html',context)

@login_required
def profilepage(request):
    return render(request,'registration/profile.html')

from django.shortcuts import render, redirect
from .models import Player

from .forms import playerform
# Create your views here.
'''def  candidate(request):
    if request.method == 'POST':
        form = playerform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/show')
    form = playerform()
    return render(request,'Administration/player_form.html',{'form': form})

def show(request):
    employees = Player.objects.all()
    return render(request,"Administration/player_list.html",{'employees':employees})
def edit(request, id):
    employee = Player.objects.get(id=id)
    return render(request,'Administration/edit.html', {'employee':employee})
def update(request, id):
    employee = Player.objects.get(id=id)
    form = playerform(request.POST, instance = employee)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request, 'Administration/edit.html', {'employee': employee})
def destroy(request, id):
    employee = Player.objects.get(id=id)
    employee.delete()
    return redirect("/show")'''

class candidate(CreateView):
    model = Player
    fields = '__all__'
    success_url = '/list'

class List(ListView):
    model=Player

class Update(UpdateView):
    model=Player
    fields='__all__'
    success_url = "/list"

class Delete(DeleteView):
    model=Player
    success_url = '/list'

from .models import Coach

class Coach_create(CreateView):
    model = Coach
    fields = '__all__'
    success_url = '/coach_list'

class Coach_List(ListView):
    model=Coach
class Coach_Update(UpdateView):
    model=Coach
    fields='__all__'
    success_url = "/coach_list"

class Coach_Delete(DeleteView):
    model=Coach
    success_url = '/coach_list'
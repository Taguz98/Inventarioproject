from django.shortcuts import render, redirect
from django.views.generic import CreateView, View
from django.http.response import HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required


from .forms import *

from .models import *
# Create your views here.

class RegistratUsuario(CreateView):
    model = Usuario
    fields = ['nombre', 'apellido', 'cedula', 'email', 'password']
    success_url = '/usuarios/'


def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
            if user.is_superuser:
                return redirect('/menu/admin/')
            else:
                return redirect('/menu/empleado/')
        else:
            return redirect('/login/')
    else:
        return render(request, 'usuarios/login.html', {})

@login_required(login_url='/login')
def Logout(request):
    logout(request)
    return redirect('/login/')

def menuAdmin(request):
    return render(request, 'usuarios/menuAdmin.html')

def menuEmpleado(request):
    return render(request, 'usuarios/menuEmpleado.html')

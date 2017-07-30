from . import nn3
from django.shortcuts import render
from django.http import HttpResponse
from .models import Patient
from .forms import PatientForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# Create your views here.


def index(request):
    return render(request, 'checker/index.html', { })


def user_login(request):
    '''
    uname = request.POST['name']
    key = request.POST['psw']
    
    try:
        if key == Patient.objects.get(fname=uname).password:
            return render(request, 'checker/checker.html', {})
        else:
            return render(request, 'checker/index.html', {'error': True })
    except:
        return render(request, 'checker/index.html', {'error': True })
     '''
    username = request.POST['name']
    password = request.POST['psw']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request,user)
            return render(request, 'checker/checker.html', {'user': user})
        else:
            return render(request, 'checker/index.html', {'error': True })
    else:
        return render(request, 'checker/index.html', {'error': True })


def user_logout(request):
    logout(request)
    return render(request, 'checker/index.html', { })
            
        
    
def register(request):
    form = PatientForm(request.POST)
    return render(request, 'checker/register.html', {'form': form})

def register2(request):
    name = request.POST['user_name']
    emailInput = request.POST['email']
    psw = request.POST['password']
    gen = request.POST['gender']
    
    p = Patient(user_name=name, email= emailInput, password=psw, gender=gen, possible_disease=' ')
    p.save()
    
    user = User.objects.create_user(username=name, password=psw)
    user.save()
    return render(request, 'checker/gotohome.html', {})


def check(request):
    ip = request.POST['q']
    diseaseDesp = []
    
    current_user = request.user
    predictedDisease = nn3.compute(ip)
    p = Patient.objects.get(user_name=current_user)
    savedDisease = p.possible_disease
    for i in predictedDisease: 
        savedDisease = savedDisease + '\n' + i
        diseaseDesp.append(Disease.objects.get(disease_name=i).description)
    p.possible_disease = savedDisease
    p.save()

    diseases = dict(zip(predictedDisease, diseaseDesp))
    return render(request, 'checker/showResult.html', {'diseases': diseases, 'user':current_user})

def profile(request):
    p = Patient.objects.get(user_name=request.user)
    return render(request, 'checker/profile.html',{ 'user' : p})
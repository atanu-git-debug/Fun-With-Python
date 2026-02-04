from django.shortcuts import render,redirect
from .forms import signupForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
# Create your views here.

def signup(request):
    
    if request.method == 'POST':
        form = signupForm(request.POST)
        if form.is_valid:
            
            form.save()
            return redirect ('home')
        else:
            print(form.errors)
    else:
        form = signupForm()

    context={
        'form' : form
    }
    return render(request,'authentication/signup.html',context)




def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = auth.authenticate(username=username, password=password)

            if user is not None:
                auth.login(request, user)   # <-- actual login
                return redirect('home')     # redirect only after success

    else:
        form = AuthenticationForm()

    context = {
        'form': form
    }
    return render(request, 'authentication/login.html', context)



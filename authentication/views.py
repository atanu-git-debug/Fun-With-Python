from django.shortcuts import render,redirect
from .forms import signupForm
# Create your views here.

def signup(request):
    
    if request.method == 'POST':
        form = signupForm(request.POST)
        if form.is_valid:
            print(form)
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
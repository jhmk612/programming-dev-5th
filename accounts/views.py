from django.shortcuts import render
from .forms import SignupForm
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect
# Create your views here.

def signup(request):
    if request.method =='POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/login')
    else:
        form=SignupForm()


    return render(request, 'accounts/signup.html', {'form':form})
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post, lnglat_validator, Zipcode
from .forms import PostForm
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth.decorators import login_required

# Create your views here.

def post_list(request):
    posts=Post.objects.all()
    context= {'posts':posts}
    return render(request, 'blog/post_list.html', context)

def intro(request):
    return render(request, 'blog/intro.html')

@login_required
def write_post(request):
    if not request.user.is_authenticated():
        return redirect(settings.LOGIN_URL)
    if request.method=='POST':
        f=PostForm(request.POST)

        new_post=f.save(commit=False)
        new_post.writer=request.user
        new_post.save()

        return HttpResponseRedirect('/')

    else:
        f=PostForm()

    return render(request, 'blog/post.html', {'form':f})










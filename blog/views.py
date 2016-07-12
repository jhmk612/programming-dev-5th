from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

def post_list(request):
    return render(request, 'blog/post_list.html')









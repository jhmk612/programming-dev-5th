from django import forms
import re
from django.forms import ValidationError
from django.utils import timezone
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields=['title', 'content', 'tags', 'lnglat']
        labels={'title':'제목', 'content':'내용', 'tags':'태그', 'lnglat':'경도, 위도'}

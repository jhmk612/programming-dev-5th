import re
from django.db import models
from django.forms import ValidationError
from django.utils import timezone
from django.conf import settings
from .validators import ZipCodeValidator


# Create your models here.
def zipcode_validator(zipcode):
    pass


class Zipcode(models.Model):
    zip_code=models.CharField(max_length=10, validators=[ZipCodeValidator(True)], help_text='우편번호를 입력')

    def __str__(self):
        return self.zip_code


def lnglat_validator(lnglat):
    if not re.match(r'^(\d+\.?\d*),(\d+\.?\d*)$', lnglat):
        raise forms.ValidationError('Invalid LngLat Type')



class Post(models.Model):
    title=models.CharField(max_length=100, verbose_name='제목')
    content=models.TextField(help_text='Markdown 문법을 써주세요.')
    tag_set=models.ManyToManyField('Tag', blank=True)
    lnglat=models.CharField(max_length=50, validators=[lnglat_validator], help_text='경도, 위도 포맷으로 입력')
    created_at=models.DateTimeField(default=timezone.now)
    test_field=models.IntegerField(default=10)
    writer = models.ForeignKey(settings.AUTH_USER_MODEL)

    def __str__(self):
        return self.title, self.created_at

class Comment(models.Model):
    post=models.ForeignKey(Post)
    message=models.TextField()
    author=models.CharField(max_length=20)

class Tag(models.Model):
    name=models.CharField(max_length=20)

    def __str__ (self):
        return self.name



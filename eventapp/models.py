from django.db import models

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=150)
    author = models.CharField(max_length=100)
    pub_date=models.DateTimeField('data published')
    photo=models.ImageField(upload_to='images/')  #기본값:False (반드시 올려야함) ->views.py def create로 가시오.
    body=models.TextField()
    def __str__(self):
        return self.title
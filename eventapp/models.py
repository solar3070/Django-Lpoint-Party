from django.db import models

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=150)
    author = models.CharField(max_length=100)
    pub_date=models.DateTimeField('data published')
    EVENT_CHOICES = (
      ('EVENT1', 'EVENT1) 손가락 인증 이벤트!'),
      ('EVENT2', 'EVENT2) L.POINT 사용 인증 이벤트!'),
      )
    event_choice = models.CharField(max_length=10, choices=EVENT_CHOICES, null=True,default='')
    photo=models.ImageField(upload_to='images/')
    body=models.TextField()
    def __str__(self):
        return self.title
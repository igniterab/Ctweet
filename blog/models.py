from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User , on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    #we can also use redirect but reverse will return address as a complete string
    #we are writing this function so the page will redirect to the home page again
    def get_absolute_url(self):
        return reverse('PostDetail',kwargs={'pk': self.pk})



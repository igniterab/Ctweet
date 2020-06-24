from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

LIKE_CHOICES = (
    ('Like','Like'),
    ('Unlike','Unlike'),
)

class PostLike(models.Model):
    user =  models.ForeignKey(User , on_delete=models.CASCADE)
    tweet =  models.ForeignKey('Post' , on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES , default='Like',max_length=10)
    time_stamp = models.DateTimeField(auto_now_add=True)


class Post(models.Model):
    post_img = models.ImageField(upload_to='media',blank=True,default='deff.jpg')
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    support = models.ManyToManyField(User , related_name='support',blank=True,through=PostLike )
    author = models.ForeignKey(User , on_delete=models.CASCADE,related_name='author')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def snippet(self):
        return self.content[:250] + "..."  

    #we can also use redirect but reverse will return address as a complete string
    #we are writing this function so the page will redirect to the home page again
    def get_absolute_url(self):
        return reverse('PostDetail',kwargs={'pk': self.pk})

    @property
    def num_likes(self):
        return self.support.all().count()




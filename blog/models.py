from django.db import models
from django.contrib.auth.models import User

class BlogPost(models.Model):
    author = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True,)
    img = models.URLField(max_length=255, null=True, blank=True)
    title = models.CharField(max_length=255, null=False, blank=False)
    sbtitle = models.CharField(max_length=255, null=True, blank=True)
    content = models.TextField(null=False, blank=False)
    content_1 = models.TextField(null=True, blank=True)
    content_2 = models.TextField(null=True, blank=True)
    content_3 = models.TextField(null=True, blank=True)
    content_4 = models.TextField(null=True, blank=True)
    content_5 = models.TextField(null=True, blank=True)
    content_6 = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.title
    

from django.db import models
from django.conf import settings

class Blog(models.Model):
    title = models.CharField(max_length=160)
    text = models.TextField()
    image = models.ImageField()
    publish_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    is_published = models.BooleanField(default=False)
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class author(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_picture= models.FileField()
    details = models.TextField()
    def __str__(self):
        return self.name.username

class category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class article(models.Model):
    article_author = models.ForeignKey(author, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    body = models.TextField()

    category = models.ForeignKey(category, on_delete=models.CASCADE)
    image = models.FileField()
    posted_on = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True, auto_now_add=False)
    def __str__(self):
        return self.title

class comment(models.Model):
    post=models.ForeignKey(article, on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    post_comment=models.TextField()
    def __str__(self):
        return self.post.title



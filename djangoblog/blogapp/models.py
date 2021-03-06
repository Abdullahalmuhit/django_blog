from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

class author(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE)
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
    body = RichTextUploadingField()

    category = models.ForeignKey(category, on_delete=models.CASCADE)
    image = models.FileField()
    posted_on = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True, auto_now_add=False)
    def __str__(self):
        return self.title

class comment(models.Model):
    post=models.ForeignKey(article, on_delete=models.CASCADE, blank=True, null=True)
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    post_comment=models.TextField()
    def __str__(self):
        return self.post.title

# article save signals
def save_article(sender, instance, **kwargs):
    print("Article is Saved")
post_save.connect(save_article, sender=article)
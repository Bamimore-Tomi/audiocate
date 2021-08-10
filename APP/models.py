from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Book(models.Model):
    link=models.CharField(max_length=225)
    name=models.TextField()
    audio=models.FileField()
    user=models.ForeignKey(User, null=True,blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Genre(models.Model):
    name=models.TextField()
    book=models.ManyToManyField(Book)

    def __str__(self):
        return self.name


class Explore(models.Model):
    name =models.TextField()
    link =models.CharField(max_length=225)
    voice =models.TextField()
    date=models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(User, null=True,blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Bookmark(models.Model):
    name =models.TextField()
    link =models.CharField(max_length=225)
    user=models.ForeignKey(User, null=True,blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    image= models.ImageField(default="team-4.jpg'")

    def __str__(self):
        return self.user

class Featured(models.Model):
    name=models.TextField()
    authors_image=models.ImageField()
    authors_email=models.TextField()
    cover_image=models.ImageField()
    title = models.TextField()
    summary = models.TextField()
    audio=models.FileField()
    link =models.CharField(max_length=225)
    state=models.BooleanField(default=False)

    def __str__(self):
        return self.title

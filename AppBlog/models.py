from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User


STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title











# Create your models here.
class Blogger(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip = models.CharField(max_length=100)
    website = models.URLField()
    company = models.CharField(max_length=100)
    about = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    
    def __str__(self):
        return f"BLOGGER: {self.name} EMAIL: {self.email} PHONE: {self.phone} ADDRESS: {self.address} CITY: {self.city} STATE: {self.state} ZIP: {self.zip} WEBSITE: {self.website} COMPANY: {self.company} ABOUT: {self.about} CREATED_AT: {self.created_at} UPDATED_AT: {self.updated_at}"
    
class Blog(models.Model):
    title = models.CharField(max_length=100)
    numero = models.IntegerField()
    description = models.TextField(max_length=500)
    blogger = models.ForeignKey(Blogger, on_delete=models.CASCADE)
    #blogger = models.ForeignKey(Blogger)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    
    def __str__(self):
        return f"BLOG: {self.title} NUMERO: {self.numero} DESCRIPTION: {self.description} BLOGGER: {self.blogger} CREATED_AT: {self.created_at} UPDATED_AT: {self.updated_at}"
    

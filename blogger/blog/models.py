from django.db import models
from django.utils.text import slugify
from django.urls import reverse

class Blogger(models.Model):
    first_name = models.CharField(max_length=100,null=True)
    last_name = models.CharField(max_length=100,null=True)
    email = models.EmailField(unique=True,null=True)
    contact = models.CharField(max_length=15, null=True, blank=True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

class Post(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField(auto_now_add=True)
    image_name = models.CharField(max_length=100)
    content = models.TextField()
    description = models.TextField()
    image = models.ImageField(upload_to='blog_images/')
    slug = models.SlugField(unique=True, blank=True)
    blogger = models.ForeignKey(Blogger, on_delete=models.CASCADE)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug': self.slug})
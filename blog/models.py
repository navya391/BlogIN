from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(max_length=100)
    post = models.TextField(max_length=10000)
    author = models.ForeignKey(User,on_delete=models.CASCADE, related_name="author")
    category = models.ForeignKey(Category,on_delete=models.CASCADE, related_name="choices")
    date = models.DateTimeField(default=datetime.now, blank=True)
    image = models.ImageField(upload_to="media/images", default="")
    like = models.ManyToManyField(User, related_name="liked_posts")
    dislikes = models.ManyToManyField(User, related_name="disliked_post")

    def __str__(self):
        return self.title

class Comment(models.Model):
    comment_by = models.ForeignKey(User,on_delete=models.CASCADE)
    comment_text = models.TextField(max_length=300)
    comment_on_blog = models.ForeignKey(Blog,on_delete=models.CASCADE, default="",related_name="comments")
    comment_time = models.DateTimeField(default=datetime.now, blank=True)
    

    
class Profile(models.Model):
    writer = models.OneToOneField(User,on_delete=models.CASCADE)
    about = models.TextField(max_length=1000)
    img = models.ImageField(upload_to="media/profilepic", default="")
    cover = models.ImageField(upload_to="media/coverpic", default="")




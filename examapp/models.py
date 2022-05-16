from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Post(models.Model):
    text = models.CharField(max_length=255)
    pub_date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user
    
    def __str__(self):
        return self.text


class Comments(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comm_text = models.CharField(max_length=255)
    
    def __str__(self):
        return self.post

    def __str__(self):
        return self.user

    def __str__(self):
        return self.comm_text


class Likes(models.Model):
    post = models.OneToOneField(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.post

    def __str__(self):
        return self.user

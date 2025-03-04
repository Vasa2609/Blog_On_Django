from django.db import models



class Post(models.Model):
    title = models.CharField(max_length=1200)
    content = models.CharField(max_length=2000)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

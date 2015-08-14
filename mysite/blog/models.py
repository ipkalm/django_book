from django.db import models

# Create your models here.

class BlogPost(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    timestamp = models.DateTimeField()

    def __repr__(self):
        return self.title

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-timestamp', 'title')


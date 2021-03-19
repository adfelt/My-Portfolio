from django.db import models

# My Models

class Blog(models.Model):
    # My models attributes
    title = models.CharField(max_length=100)
    date_posted = models.DateTimeField()
    text_body = models.TextField()
    image = models.ImageField(upload_to='images/')

from django.db import models

# My Models

class Blog(models.Model):
    # My models attributes
    title = models.CharField(max_length=100)
    date_posted = models.DateTimeField()
    text_body = models.TextField()
    image = models.ImageField(upload_to='images/')

    def summary(self):
        return self.text_body[:260]

    def pub_date_pretty(self):
        return self.date_posted.strftime('%b %e %Y')

    def __str__(self):
        return self.title




from django.db import models

class Aboutme(models.Model):

    title = models.CharField(max_length=100)
    content = models.TextField()
    footer_content = models.TextField()

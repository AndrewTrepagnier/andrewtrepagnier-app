from django.db import models

class HomePage(models.Model):

    title = models.CharField(max_length=100)
    description = models.TextField()
    footer_content = models.TextField()

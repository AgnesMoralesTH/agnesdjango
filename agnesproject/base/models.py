from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField(max_length=254)
    topic = models.CharField(max_length=150)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.topic
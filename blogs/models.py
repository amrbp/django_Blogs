from django.db import models

# Create your models here.

CHOICES = (
        ('Art', 'Art'),
        ('Animal', 'Animal'),
        ('IT', 'IT'),
        ('News', 'News'),
        ('Sport', 'Sport'),
        ('Other', 'Other'),
    )

class Post(models.Model):
    username = models.CharField(max_length=300)
    title= models.CharField(max_length=300, unique=True)
    category = models.CharField(max_length=300, choices = CHOICES)
    image = models.ImageField(upload_to='image')
    content= models.TextField() 

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.__str__()


from django.db import models

# Create your models here.
class profile(models.Model):
    first_name = models.CharField(max_length=50)
class posts(models.Model):
    POST_TYPE = (
        ('I', 'Image'),
        ('T', 'Text'),
        ('L', 'Link')
    )
    }
    account = models.ForeignKey(profile, on_delete=models.CASCADE)

    type = models.CharField(max_length=1, choice=POST_TYPE)
    title = models.CharField(max_length=50)
    text= models.CharField(max_length=100)

    release_date = models.DateField()

    likes = models.IntegerField
    shares = models.IntegerField



class comment(models.Model):
    post = model.ForeignKey(posts, on_delete=models.CASCADE)

from django.db import models

# Create your models here.
class Tweet(models.Model):
    tweet = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.tweet


class Sample(models.Model):
    name = models.CharField(max_length=16)
from django.db import models


class Post(models.Model):
    commit= models.CharField(max_length=50,unique=True)
    like = models.IntegerField(default=True)
   
    def __str__(self):
        return self.commit


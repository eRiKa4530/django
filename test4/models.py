from django.db import models
from test3.models import Post

class Commint(models.Model):
    commit= models.CharField(max_length=50,unique=True)
    category = models.ForeignKey(Post,on_delete= models.CASCADE,related_name='commints')
    def __str__(self):
        return self.commit


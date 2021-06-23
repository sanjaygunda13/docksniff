from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class producs(models.Model):
    id = models.AutoField(primary_key = True)
    products_name = models.CharField(max_length=20,default="cars")
    user = models.ForeignKey(
        User,  on_delete = models.CASCADE)
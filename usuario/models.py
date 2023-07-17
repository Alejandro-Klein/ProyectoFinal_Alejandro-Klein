from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Clave foranea es la id que relaciona dos modelos diferentes de la base de datos sql.

class InfoExtra(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatares',null=True,blank=True)
    
 
    
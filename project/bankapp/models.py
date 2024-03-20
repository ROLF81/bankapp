from django.db import models

class Member(models.Model):
    ID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    email = models.CharField(max_length=128)
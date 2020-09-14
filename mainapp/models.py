from django.db import models


class Users(models.Model):
    id = models.fields.IntegerField(auto_created=True, primary_key=True)
    first_name = models.fields.CharField(max_length=45, null=False)
    last_name = models.fields.CharField(max_length=45, null=False)
    age = models.fields.IntegerField()

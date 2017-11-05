from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class user_files(models.Model):
    Filename = models.CharField(max_length=50)
    Browse = models.FileField(upload_to='img/')
    user_uploaded = models.ForeignKey(User, related_name='file_owner')
    shared_with = models.ManyToManyField(User,related_name='shared_file')

    def get_absolute_url(self):
        return '/img/%s' % self.Browse.name


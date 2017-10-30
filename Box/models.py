from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class user_files(models.Model):
    Filename = models.CharField(max_length=50)
    Browse = models.FileField(upload_to='img/')
    user_uploaded = models.CharField(max_length=50, blank=True)

    def get_absolute_url(self):
        return '/img/%s' % self.Browse.name

user_list = (User.objects.all())

class share_files(models.Model):
    select_file = models.CharField(max_length=300)
    from_user = models.CharField(max_length=50)
    select_user = models.CharField(max_length=50,default=None)

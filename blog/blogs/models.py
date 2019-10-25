from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Bolg_type(models.Model):
    type_name = models.CharField(max_length=64)

    def __str__(self):
        return self.type_name


class Bolgs(models.Model):
    title = models.CharField(max_length=128)
    blog_type = models.ForeignKey(Bolg_type, on_delete=models.DO_NOTHING)
    content = models.TextField(max_length=1024)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    created_time = models.DateTimeField(auto_now_add=True)
    last_update_time = models.TimeField(auto_now=True)

    def __str__(self):
        return '<blog: %s>' % self.title

    class Meta:
        ordering = ['-created_time']
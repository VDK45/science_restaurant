from django.db import models

# Create your models here.


class Visitor(models.Model):
    nik_name = models.CharField(max_length=255)
    about = models.TextField(blank=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return f'Name {self.nik_name} - {self.about}'

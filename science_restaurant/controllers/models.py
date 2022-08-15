from django.db import models

# Create your models here.
from django.urls import reverse


class Visitor(models.Model):
    nik_name = models.CharField(max_length=255)
    about = models.TextField(blank=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return f'Name {self.nik_name} - {self.about}'

    def get_absolute_url(self):
        return reverse('news', kwargs={'news_id': self.pk})


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name


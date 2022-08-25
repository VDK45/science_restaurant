from django.db import models

# Create your models here.
from django.urls import reverse


class Visitor(models.Model):
    nik_name = models.CharField(max_length=255, verbose_name='Name')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    about = models.TextField(blank=True, verbose_name='About')
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name='Photo')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Created at')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Updated at')
    is_published = models.BooleanField(default=True, verbose_name='Published')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Category')

    def __str__(self):
        return f'Name {self.nik_name} - {self.about}'

    def get_absolute_url(self):
        return reverse('news', kwargs={'news_slug': self.slug})

    class Meta:
        verbose_name = 'Visitor'
        verbose_name_plural = 'Visitors'
        ordering = ['time_create', 'nik_name']


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Category')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # return reverse('category', kwargs={'cat_id': self.pk})  # For function views.show_category
        return reverse('category', kwargs={'cat_slug': self.slug})  # For class RestaurantCategory

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Category'
        ordering = ['id']

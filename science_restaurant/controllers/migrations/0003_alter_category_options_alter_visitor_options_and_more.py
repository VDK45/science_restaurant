# Generated by Django 4.1 on 2022-08-17 06:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('controllers', '0002_category_visitor_cat'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['id'], 'verbose_name': 'Category', 'verbose_name_plural': 'Category'},
        ),
        migrations.AlterModelOptions(
            name='visitor',
            options={'ordering': ['time_create', 'nik_name'], 'verbose_name': 'Visitor', 'verbose_name_plural': 'Visitors'},
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(db_index=True, max_length=100, verbose_name='Category'),
        ),
        migrations.AlterField(
            model_name='visitor',
            name='about',
            field=models.TextField(blank=True, verbose_name='About'),
        ),
        migrations.AlterField(
            model_name='visitor',
            name='cat',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='controllers.category', verbose_name='Category'),
        ),
        migrations.AlterField(
            model_name='visitor',
            name='is_published',
            field=models.BooleanField(default=True, verbose_name='Published'),
        ),
        migrations.AlterField(
            model_name='visitor',
            name='nik_name',
            field=models.CharField(max_length=255, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='visitor',
            name='photo',
            field=models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Photo'),
        ),
        migrations.AlterField(
            model_name='visitor',
            name='time_create',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created at'),
        ),
        migrations.AlterField(
            model_name='visitor',
            name='time_update',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated at'),
        ),
    ]

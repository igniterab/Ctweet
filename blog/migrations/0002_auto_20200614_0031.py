# Generated by Django 3.0.7 on 2020-06-13 19:01

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='no_support',
            field=models.ManyToManyField(blank=True, related_name='unlikes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='post',
            name='post_img',
            field=models.ImageField(blank=True, default='deff.jpg', upload_to='post_pics'),
        ),
        migrations.AddField(
            model_name='post',
            name='support_it',
            field=models.ManyToManyField(blank=True, related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
    ]

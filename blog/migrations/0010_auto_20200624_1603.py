# Generated by Django 3.0.7 on 2020-06-24 10:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0009_auto_20200624_1535'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='no_support',
        ),
        migrations.AddField(
            model_name='postlike',
            name='value',
            field=models.CharField(choices=[('Like', 'Like'), ('Unlike', 'Unlike')], default='Like', max_length=10),
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='support',
            field=models.ManyToManyField(blank=True, related_name='support', through='blog.PostLike', to=settings.AUTH_USER_MODEL),
        ),
    ]

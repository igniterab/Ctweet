# Generated by Django 3.0.7 on 2020-06-23 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20200623_1518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_img',
            field=models.ImageField(blank=True, default='deff.jpg', upload_to='profile_pics'),
        ),
    ]

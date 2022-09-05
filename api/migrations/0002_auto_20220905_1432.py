# Generated by Django 3.2.15 on 2022-09-05 11:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='image_path',
        ),
        migrations.AddField(
            model_name='image',
            name='image',
            field=models.ImageField(default='media/default_image.png', max_length=120, upload_to=''),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='author_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

# Generated by Django 3.0.6 on 2020-09-15 17:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0002_auto_20200915_1646'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='content',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
# Generated by Django 5.0.6 on 2024-06-20 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0002_remove_producto_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='productos/'),
        ),
    ]

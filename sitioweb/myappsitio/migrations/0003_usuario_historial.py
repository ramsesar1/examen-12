# Generated by Django 4.2.7 on 2023-11-29 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myappsitio', '0002_usuario_is_active_usuario_is_staff_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='historial',
            field=models.JSONField(default=list),
        ),
    ]

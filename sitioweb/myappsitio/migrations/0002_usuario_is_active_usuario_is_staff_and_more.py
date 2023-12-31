# Generated by Django 4.2.7 on 2023-11-29 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myappsitio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='usuario',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='password',
            field=models.CharField(default='password123', max_length=128, verbose_name='password'),
            preserve_default=False,
        ),
    ]

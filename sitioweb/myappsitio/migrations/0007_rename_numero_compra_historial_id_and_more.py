# Generated by Django 4.2.7 on 2023-12-03 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myappsitio', '0006_alter_historial_precio_total'),
    ]

    operations = [
        migrations.RenameField(
            model_name='historial',
            old_name='numero_compra',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='historial',
            old_name='detalles',
            new_name='orden',
        ),
        migrations.RemoveField(
            model_name='historial',
            name='fecha',
        ),
        migrations.AddField(
            model_name='historial',
            name='nombre',
            field=models.CharField(default='exit', max_length=255),
            preserve_default=False,
        ),
    ]

# Generated by Django 4.2.6 on 2023-10-22 23:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_rename_admin_entidad_administrador'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comunicado',
            name='entidad',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.entidad'),
        ),
    ]

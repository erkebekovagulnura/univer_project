# Generated by Django 3.1.3 on 2020-11-16 06:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Groups_faculties', '0001_initial'),
        ('Shcedule', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shcedule',
            name='group',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Groups_faculties.groups'),
        ),
    ]
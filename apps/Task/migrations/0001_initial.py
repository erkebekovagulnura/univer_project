# Generated by Django 3.1.3 on 2020-11-15 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('created_ad', models.DateTimeField(auto_now_add=True)),
                ('email', models.EmailField(max_length=254)),
                ('deadline', models.DateField(blank=True, null=True)),
                ('done', models.BooleanField(default=False)),
                ('verified', models.BooleanField(default=False)),
            ],
        ),
    ]

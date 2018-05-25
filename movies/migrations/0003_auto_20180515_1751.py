# Generated by Django 2.0.1 on 2018-05-15 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_schedule'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schedule',
            name='movies',
        ),
        migrations.AddField(
            model_name='schedule',
            name='movies',
            field=models.ManyToManyField(to='movies.Movie'),
        ),
    ]

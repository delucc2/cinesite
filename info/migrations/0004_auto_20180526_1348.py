# Generated by Django 2.0.1 on 2018-05-26 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0003_auto_20180526_1151'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='director',
            field=models.CharField(default='John Cena', max_length=200),
        ),
        migrations.AddField(
            model_name='movie',
            name='poster',
            field=models.ImageField(default='home/static/home/images/logo.png', upload_to=''),
        ),
        migrations.AddField(
            model_name='movie',
            name='rating',
            field=models.CharField(choices=[('G', 'G'), ('PG', 'PG'), ('PG-13', 'PG-13'), ('R', 'R')], default='PG-13', max_length=5),
        ),
        migrations.AddField(
            model_name='movie',
            name='runtime',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='movie',
            name='trailer_src',
            field=models.CharField(default='https://www.youtube.com/watch?v=m55BwMitHNw', max_length=1000),
        ),
    ]

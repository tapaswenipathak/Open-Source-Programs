# Generated by Django 2.2.1 on 2019-05-10 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0006_auto_20190509_1956'),
    ]

    operations = [
        migrations.CreateModel(
            name='osc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('osc_homepage', models.URLField(default=None)),
                ('awards', models.CharField(max_length=50)),
                ('timeline', models.URLField(blank=True)),
            ],
        ),
    ]

# Generated by Django 2.2.4 on 2020-12-13 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0004_auto_20201213_2344'),
    ]

    operations = [
        migrations.CreateModel(
            name='Explore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('link', models.CharField(max_length=225)),
                ('voice', models.TextField()),
            ],
        ),
    ]

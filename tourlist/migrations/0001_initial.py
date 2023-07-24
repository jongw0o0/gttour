# Generated by Django 4.2.3 on 2023-07-24 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tourmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=100)),
                ('location_code', models.CharField(max_length=5)),
                ('positive', models.TextField()),
                ('negative', models.TextField()),
                ('image', models.ImageField(upload_to='')),
                ('tour_loc', models.TextField()),
            ],
        ),
    ]
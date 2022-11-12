# Generated by Django 4.1 on 2022-10-08 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('dob', models.CharField(max_length=50)),
                ('gen', models.CharField(max_length=50)),
                ('locality', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('code', models.PositiveIntegerField()),
                ('state', models.CharField(max_length=50)),
                ('mob', models.PositiveIntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('jobloc', models.CharField(max_length=50)),
                ('img', models.ImageField(blank=True, default=None, null=True, upload_to='profile_img/')),
                ('doc', models.FileField(blank=True, default=None, null=True, upload_to='docs/')),
            ],
        ),
    ]
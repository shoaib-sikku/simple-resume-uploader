# Generated by Django 4.1 on 2022-10-08 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_resume_dob_alter_resume_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='dob',
            field=models.CharField(max_length=50),
        ),
    ]
# Generated by Django 4.2.6 on 2024-01-01 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_rename_userprofile_userprofiledetail'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profiledetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.DeleteModel(
            name='Userprofiledetail',
        ),
    ]

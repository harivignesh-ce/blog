# Generated by Django 3.2.8 on 2021-10-12 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(default=None, max_length=254, null=True),
        ),
    ]
# Generated by Django 4.2.7 on 2023-12-05 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_manage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='isbn',
            field=models.IntegerField(),
        ),
    ]

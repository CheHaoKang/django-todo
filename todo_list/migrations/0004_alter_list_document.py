# Generated by Django 4.1.2 on 2022-12-09 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0003_alter_list_document'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='document',
            field=models.FileField(null=True, upload_to='documents/'),
        ),
    ]

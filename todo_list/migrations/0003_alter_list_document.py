# Generated by Django 4.1.2 on 2022-12-09 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0002_alter_list_document'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='document',
            field=models.FileField(default=False, null=True, upload_to='documents/'),
        ),
    ]
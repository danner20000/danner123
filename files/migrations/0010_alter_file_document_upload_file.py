# Generated by Django 4.1 on 2023-10-17 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0009_file_document_agency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file_document',
            name='upload_file',
            field=models.FileField(upload_to='static/img'),
        ),
    ]

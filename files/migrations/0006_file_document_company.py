# Generated by Django 4.1 on 2023-10-09 07:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_company_company_name'),
        ('files', '0005_file_document_department_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='file_document',
            name='company',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.company'),
        ),
    ]

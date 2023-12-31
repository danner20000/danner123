# Generated by Django 4.1 on 2023-10-03 02:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='File_Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('select_BU', models.CharField(choices=[('fishing company', 'Fishing Company'), ('holy child', 'Holy Child'), ('sto. niño', 'Sto. Niño')], default='Select Company', max_length=50)),
                ('document_type', models.CharField(choices=[('contract', 'Contract'), ('invoice', 'Invoice'), ('report', 'Report')], default='Select Document Type', max_length=50)),
                ('department', models.CharField(choices=[('department of health', 'Department of Health'), ('human resource', 'Human Resource'), ('registrar', 'Registrar')], default='Select Department', max_length=50)),
                ('upload_file', models.FileField(upload_to='save_img')),
                ('renewal_date', models.DateField()),
                ('expiry_date', models.DateField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

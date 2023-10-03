from django.db import models

# Create your models here.
class Files(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)

    select_BU = models.CharField(
        max_length=50,
        choices=[
            ('fishing company', 'Fishing Company'),
            ('holy child', 'Holy Child'),
            ('sto. niño', 'Sto. Niño'),
            # Add more choices as needed
        ],
        default='Select Company' 
    )

    document_type = models.CharField(
        max_length=50,
        choices=[
            ('contract', 'Contract'),
            ('invoice', 'Invoice'),
            ('report', 'Report'),
            # Add more choices as needed
        ],
        default='Select Document Type' 
    )

    department = models.CharField(
        max_length=50,
        choices=[
            ('department of health', 'Department of Health'),
            ('human resource', 'Human Resource'),
            ('registrar', 'Registrar'),
            # Add more choices as needed
        ],
        default='Select Department'  
    )

    upload_file = models.FileField(upload_to='save_img')
    renewal_date = models.DateField()
    expiry_date = models.DateField()

    def __str__(self):
        return self.user.email

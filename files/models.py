from django.db import models
# Create your models here.

class Department(models.Model):
    department_name = models.CharField(max_length=50, null=True)
    company = models.ForeignKey('users.Company', on_delete=models.CASCADE)

    def __str__(self):
        return self.department_name
    
    class Meta:
        unique_together = ('department_name', 'company')

class File_Document(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    company = models.ForeignKey('users.Company', on_delete=models.CASCADE, default=1) 
    department_name = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)

    document_type = models.CharField(
        max_length=50,
        choices=[
            ('contract', 'Contract'),
            ('invoice', 'Invoice'),
            ('report', 'Report'),
        ],
        default='Select Document Type' 
    )
    agency = models.CharField(max_length=50, default='Default Agency Name')
    upload_file = models.FileField(upload_to='static/img')
    renewal_date = models.DateField()
    expiry_date = models.DateField()

    def __str__(self):
        return self.document_type
    
    def delete(self):
        self.upload_file.delete()
        super().delete()

class FileLog(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    file_document = models.ForeignKey(File_Document, on_delete=models.CASCADE)
    action = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.email} {self.action} {self.file_document}"
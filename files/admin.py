from django.contrib import admin

from .models import File_Document
# Register your models here.
@admin.register(File_Document)
class File_Document_Admin(admin.ModelAdmin):
    search_fields = ('id', 'email',)
    list_display = ('id', 'select_BU','department','document_type','renewal_date', 'expiry_date')
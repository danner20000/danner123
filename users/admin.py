from django.contrib import admin
from .models import User
# Register your models here.
@admin.register(User)
class ProjectAdmin(admin.ModelAdmin):
    search_fields = ('id', 'first_name',)
    list_display = ('id', 'first_name','last_name','email')
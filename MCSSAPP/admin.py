from django.contrib import admin
from MCSSAPP.models import Post, Senior_Management_Image




# Register your models here.

class SeniorManagementAdmin(admin.ModelAdmin):
    readonly = ('image_id',)
    search_fields = ['name','position']


admin.site.register(Post)
admin.site.register(Senior_Management_Image)



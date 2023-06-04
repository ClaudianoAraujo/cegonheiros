from django.contrib import admin
from .models import BlogPost
# Register your models here.
admin.site.register(BlogPost)
admin.site.site_title = 'Cegonheiro'
admin.site.site_header = 'Cegonheiros'
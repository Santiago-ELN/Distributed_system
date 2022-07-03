from django.contrib import admin
from .models import JobCategory, Referencias, Jobs

admin.site.register(Referencias)
admin.site.register(Jobs)
admin.site.register(JobCategory)
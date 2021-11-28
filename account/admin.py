from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from user_profile.models import UserProfile

# Register your models here.
from . models import User

#admin.site.register(User)
admin.site.register(User,ImportExportModelAdmin)
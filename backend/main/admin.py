from django.contrib import admin

from main.models import Profile, CustomerProfile, AdminProfile, ManagerProfile

admin.site.register(Profile)
admin.site.register(CustomerProfile)
admin.site.register(AdminProfile)
admin.site.register(ManagerProfile)

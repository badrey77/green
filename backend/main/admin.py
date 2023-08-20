from django.contrib import admin
from django.contrib.admin import ModelAdmin, StackedInline
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

from main.models import Profile, CustomerProfile, AdminProfile, ManagerProfile


class ProfileInlineMixin(object):
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'


class CustomerProfileInline(ProfileInlineMixin, StackedInline):
    model = CustomerProfile


class AdminProfileInline(ProfileInlineMixin, StackedInline):
    model = AdminProfile


class ManagerProfileInline(ProfileInlineMixin, StackedInline):
    model = ManagerProfile


class UserAdmin(ModelAdmin):
    def get_inlines(self, request, obj):
        if obj is None:
            return []
        try:
            if obj.profile.type == 'C':
                return [CustomerProfileInline]
            elif obj.profile.type == 'M':
                return [ManagerProfileInline]
            elif obj.profile.type == 'A':
                return [AdminProfileInline]
        except ObjectDoesNotExist:
            return []


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Profile)
admin.site.register(CustomerProfile)
admin.site.register(AdminProfile)
admin.site.register(ManagerProfile)

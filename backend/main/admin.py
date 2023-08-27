from django.contrib import admin
from django.contrib.admin import ModelAdmin, StackedInline, TabularInline
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.utils.safestring import mark_safe

from main.models import Profile, CustomerProfile, AdminProfile, ManagerProfile, Restaurant, Menu, MenuItem, Dish, \
    Ingredient, IngredientQuantity, DishBase


class MenuInline(TabularInline):
    def goto(self,obj):
        if obj is not None:
            return mark_safe(f'<a href="/main/menus/{obj.pk}">Go to</a>')
    model = Menu
    extra = 0
    readonly_fields = ['goto']


@admin.register(Restaurant)
class RestaurantConfig(ModelAdmin):
    inlines = [MenuInline]


class MenuItemInline(StackedInline):
    model = MenuItem
    extra = 1
    filter_horizontal = ["dishes"]
    fieldsets = [
        (None, {
        "classes":["collapse", "collapsed"],
        "fields":[("label", "description"), "dishes", "mode"]
        }),
    ]

    class Media:
        js = ['/static/js/menuiteminline.js']



@admin.register(Menu)
class MenuConfig(ModelAdmin):
    inlines = [MenuItemInline]


class IngredientInline(TabularInline):
    model = IngredientQuantity
    extra = 0
    autocomplete_fields = ['ingredient']


@admin.register(DishBase)
class DishBaseConfig(ModelAdmin):
    search_fields = ['description', 'ingredients']


@admin.register(Dish)
class DishConfig(ModelAdmin):
    def image(self, obj):
        if obj == None:
            return
        return mark_safe(f'<img src="{obj.img}" width="400px" height="400px" alt="Image here" />')

    def thumb(self, obj):
        if obj == None:
            return
        return mark_safe(f'<img src="{obj.img}" width="80px" height="80px" alt="Thumb here" />')

    inlines = [IngredientInline]
    readonly_fields = ['image', 'thumb']
    list_display = ['label', 'type', 'thumb', 'price']



@admin.register(Ingredient)
class IngredientConfig(ModelAdmin):
    search_fields = ['label']

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

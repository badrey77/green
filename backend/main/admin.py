from django.contrib import admin
from django.contrib.admin import ModelAdmin, StackedInline, TabularInline
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.utils.safestring import mark_safe

from main.forms import DishofManForm
from main.models import Profile, CustomerProfile, AdminProfile, ManagerProfile, Restaurant, Menu, MenuItem, Dish, \
    Ingredient, IngredientQuantity, DishBase, MenuofRestaurant, RestaurantofMan, DishofMan


class MenuInline(TabularInline):
    def goto(self,obj):
        if obj is not None:
            return mark_safe(f'<a href="/admin/main/menu/{obj.pk}">Go to</a>')
    model = Menu
    extra = 0
    readonly_fields = ['goto']


@admin.register(Restaurant)
class RestaurantConfig(ModelAdmin):
    inlines = [MenuInline]


@admin.register(RestaurantofMan)
class RestaurantofManConfig(ModelAdmin):
    inlines = [MenuInline]

    def get_queryset(self, request):
        current_user = request.user
        my_restaurant = Restaurant.objects.filter(managerprofile__user=current_user).first()
        qs = super().get_queryset(request).filter(id=my_restaurant.id)
        return qs


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
    list_filter = ['restaurant']
    inlines = [MenuItemInline]
    list_display = ['label', 'restaurant', 'customizable']


@admin.register(MenuofRestaurant)
class MenuConfig(ModelAdmin):
    list_filter = ['restaurant']
    inlines = [MenuItemInline]
    list_display = ['label', 'restaurant', 'customizable']

    def get_queryset(self, request):
        current_user = request.user
        my_restaurant = Restaurant.objects.filter(managerprofile__user=current_user).first()
        qs = super().get_queryset(request).filter(restaurant=my_restaurant)
        return qs


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


@admin.register(DishofMan)
class DishofManConfig(ModelAdmin):
    def get_queryset(self, request):
        current_user = request.user
        my_restaurant = Restaurant.objects.filter(managerprofile__user=current_user).first()
        qs = super().get_queryset(request).filter(restaurant=my_restaurant)
        return qs

    def thumb(self, obj):
        if obj == None:
            return
        return mark_safe(f'<img src="{obj.img}" width="80px" height="80px" alt="Thumb here" />')

    inlines = [IngredientInline]
    readonly_fields = ['thumb']
    list_display = ['label', 'type', 'thumb', 'price']
    form = DishofManForm



@admin.register(Ingredient)
class IngredientConfig(ModelAdmin):
    def get_more_info(self, obj):
        if obj != None:
            return  mark_safe('<input id="get_more_info_btn" type="button" value="Get more info" />')
        return ''
    readonly_fields = ['get_more_info']
    search_fields = ['label']

    class Media:
        js = ['js/get_more_info.js']


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

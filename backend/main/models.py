from django.contrib.auth.models import User
from django.db import models
from django.db.models import CharField, ManyToManyField, ForeignKey, FloatField, CASCADE, BooleanField, OneToOneField, \
    IntegerField
from django.db.models.signals import post_save
from django.dispatch import receiver

DISH_TYPE = (
    ('ETR', 'Entré'),
    ('SDH', 'Side Dish'),
    ('SLD', 'Salad'),
    ('FRT', 'Fruit'),
    ('DRK', 'Drink'),
)


class Ingredient(models.Model):
    label = CharField(max_length=1000)

    def __str__(self):
        return self.label


class Restaurant(models.Model):
    label = CharField(max_length=1000)
    address = CharField(max_length=1000)
    location = CharField(max_length=255)

    def __str__(self):
        return '{} at {}'.format(self.label, self.address)


class Menu(models.Model):
    label = CharField(max_length=1000)
    description = CharField(max_length=1000)
    restaurant = ForeignKey(Restaurant, on_delete=CASCADE)
    customizable = BooleanField(default=True)

    def __str__(self):
        return self.label


class Mode(models.Model):
    label = CharField(max_length=1000)
    description = CharField(max_length=1000)

    def __str__(self):
        return self.label


class MenuItem(models.Model):
    label = CharField(max_length=1000)
    description = CharField(max_length=1000)
    dishes = ManyToManyField('Dish')
    menu = ForeignKey(Menu, on_delete=CASCADE)
    mode = ForeignKey(Mode, blank=True, null=True, on_delete=CASCADE)

    def __str__(self):
        if self.dishes.count() == 0:
            return self.label
        return '{} : {} .'.format(self.label, '-'.join([str(dish) for dish in self.dishes.all()]))


class Dish(models.Model):
    label = CharField(max_length=1000)
    description = CharField(max_length=1000)
    type = CharField(max_length=3, choices=DISH_TYPE)
    ingredients = ManyToManyField(Ingredient, through='IngredientQuantity')

    def __str__(self):
        return '{} ({})'.format(self.label, self.type)


class IngredientQuantity(models.Model):
    ingredient = ForeignKey(Ingredient, on_delete=CASCADE)
    dish = ForeignKey(Dish, on_delete=CASCADE)
    quantity = FloatField(default=100.0)

    def __str__(self):
        return '*'


PROFILE_TYPE = (
    ('M', 'Manager'),
    ('C', 'Customer'),
    ('A', 'Admin'),
)


class Profile(models.Model):
    user = OneToOneField(User, on_delete=models.CASCADE, null=True)
    type = CharField(max_length=1, choices=PROFILE_TYPE, default='C')

    def __str__(self):
        if self.user is None:
            return ''
        return '{} profile'.format(self.user.username)


class AdminProfile(Profile):
    @classmethod
    def is_super(cls):
        return super().user.is_superuser

    def __str__(self):
        return 'Admin Profile'


class CustomerProfile(Profile):
    dietary_preferences = ManyToManyField(Ingredient, related_name='preferred_customers', blank=True)
    allergies = ManyToManyField(Ingredient, related_name='allergic_customers', blank=True)
    loyalty_points = IntegerField(default=0)

    def __str__(self):
        return 'Customer Profile'


class ManagerProfile(Profile):
    restaurant = ForeignKey(Restaurant, on_delete=CASCADE, null=True, blank=True)

    def __str__(self):
        return 'Manager Profile'


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        CustomerProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if instance.profile:
        if instance.profile.type != 'C' and isinstance(instance.profile, CustomerProfile):
            tpe = instance.profile.type
            instance.profile.delete()
            if tpe == 'A':
                AdminProfile.objects.create(user=instance,type='A')
            elif tpe == 'M':
                ManagerProfile.objects.create(user=instance,type='M')


class Order(models.Model):
    user = ForeignKey(User, related_name="orders", on_delete=CASCADE)
    restaurant = ForeignKey(User, related_name="orders", on_delete=CASCADE)
    total = FloatField(default=0)
    fulfilled = BooleanField(default=False)
    items = ManyToManyField(Dish)



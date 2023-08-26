from rest_framework import serializers
from rest_framework.relations import StringRelatedField

from .models import User, Ingredient, Restaurant, Menu, Mode, DishBase, Dish, MenuItem, IngredientQuantity, Profile, AdminProfile, CustomerProfile, ManagerProfile, Order, Tag, SocialAccount, OrderedDish

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class IngredientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'

class RestaurantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Restaurant
        fields = ('id', 'label', 'address', 'location', 'menus',)


class ModeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Mode
        fields = '__all__'

class DishBaseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DishBase
        fields = '__all__'



class DishSerializer(serializers.HyperlinkedModelSerializer):
    ingredients = StringRelatedField(many=True)
    class Meta:
        model = Dish
        fields = ['id', 'label', 'description', 'img', 'price','ingredients']


class MenuItemSerializer(serializers.HyperlinkedModelSerializer):
    dishes = DishSerializer(many=True)
    class Meta:
        model = MenuItem
        fields = '__all__'


class MenuSerializer(serializers.HyperlinkedModelSerializer):
    menuitems = MenuItemSerializer(many=True, allow_null=True)
    class Meta:
        model = Menu
        fields = ['id','label','description','restaurant','customizable','menuitems']


class IngredientQuantitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = IngredientQuantity
        fields = ['id', 'ingredient', 'dish', 'quantity']


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class AdminProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AdminProfile
        fields = '__all__'

class CustomerProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomerProfile
        fields = '__all__'

class ManagerProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ManagerProfile
        fields = '__all__'

class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class SocialAccountSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SocialAccount
        fields = '__all__'

class OrderedDishSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OrderedDish
        fields = '__all__'

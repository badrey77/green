from rest_framework import serializers
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
        fields = '__all__'

class MenuSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'

class ModeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Mode
        fields = '__all__'

class DishBaseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DishBase
        fields = '__all__'

class DishSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dish
        fields = '__all__'

class MenuItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MenuItem
        fields = '__all__'

class IngredientQuantitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = IngredientQuantity
        fields = '__all__'

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

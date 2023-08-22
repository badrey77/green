#
# class Home(View):
#     @staticmethod
#     def get(request):
#         if request.method == 'GET' and 'search_query' in request.GET:
#             data = Restaurant.objects.all()
#             return render(request, template_name='./main/home.html',
#                           context={'title': 'Welcome ! Can I help you ?', 'results': data })
#
#         form = HomeSearchForm()
#         return render(request, template_name='./main/home.html', context={'form': form, 'title': 'Welcome\
#         ! Can I help you ?'})
#
from django.contrib.auth.models import PermissionsMixin
from rest_framework import viewsets, permissions

from .models import User, Ingredient, Restaurant, Menu, Mode, DishBase, Dish, MenuItem, IngredientQuantity, Profile, \
    AdminProfile, CustomerProfile, ManagerProfile, Order, Tag, SocialAccount, OrderedDish
from .serializers import UserSerializer, IngredientSerializer, RestaurantSerializer, MenuSerializer, ModeSerializer, \
    DishBaseSerializer, DishSerializer, MenuItemSerializer, IngredientQuantitySerializer, ProfileSerializer, \
    AdminProfileSerializer, CustomerProfileSerializer, ManagerProfileSerializer, OrderSerializer, TagSerializer, \
    SocialAccountSerializer, OrderedDishSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    permission_classes = [permissions.IsAuthenticated]


class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = [permissions.IsAuthenticated]


class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [permissions.IsAuthenticated]


class ModeViewSet(viewsets.ModelViewSet):
    queryset = Mode.objects.all()
    serializer_class = ModeSerializer
    permission_classes = [permissions.IsAuthenticated]


class DishBaseViewSet(viewsets.ModelViewSet):
    queryset = DishBase.objects.all()
    serializer_class = DishBaseSerializer
    permission_classes = [permissions.IsAuthenticated]


class DishViewSet(viewsets.ModelViewSet):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    permission_classes = [permissions.IsAuthenticated]


class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [permissions.IsAuthenticated]


class IngredientQuantityViewSet(viewsets.ModelViewSet):
    queryset = IngredientQuantity.objects.all()
    serializer_class = IngredientQuantitySerializer
    permission_classes = [permissions.IsAuthenticated]


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]


class AdminProfileViewSet(viewsets.ModelViewSet):
    queryset = AdminProfile.objects.all()
    serializer_class = AdminProfileSerializer
    permission_classes = [permissions.IsAuthenticated]


class CustomerProfileViewSet(viewsets.ModelViewSet):
    queryset = CustomerProfile.objects.all()
    serializer_class = CustomerProfileSerializer
    permission_classes = [permissions.IsAuthenticated]


class ManagerProfileViewSet(viewsets.ModelViewSet):
    queryset = ManagerProfile.objects.all()
    serializer_class = ManagerProfileSerializer
    permission_classes = [permissions.IsAuthenticated]


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [permissions.IsAuthenticated]


class SocialAccountViewSet(viewsets.ModelViewSet):
    queryset = SocialAccount.objects.all()
    serializer_class = SocialAccountSerializer
    permission_classes = [permissions.IsAuthenticated]


class OrderedDishViewSet(viewsets.ModelViewSet):
    queryset = OrderedDish.objects.all()
    serializer_class = OrderedDishSerializer
    permission_classes = [permissions.IsAuthenticated]

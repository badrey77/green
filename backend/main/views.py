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
import requests
from django.db.models.functions import Lower
from django.http import HttpResponse, JsonResponse
from django.views import View
from rest_framework import viewsets, permissions
from rest_framework.utils import json

from .models import User, Ingredient, Restaurant, Menu, Mode, DishBase, Dish, MenuItem, IngredientQuantity, Profile, \
    AdminProfile, CustomerProfile, ManagerProfile, Order, Tag, SocialAccount, OrderedDish
from .serializers import UserSerializer, IngredientSerializer, RestaurantSerializer, MenuSerializer, ModeSerializer, \
    DishBaseSerializer, DishSerializer, MenuItemSerializer, IngredientQuantitySerializer, ProfileSerializer, \
    AdminProfileSerializer, CustomerProfileSerializer, ManagerProfileSerializer, OrderSerializer, TagSerializer, \
    SocialAccountSerializer, OrderedDishSerializer


class Search(View):
    @staticmethod
    def get(request):
        params = {
            #'nutrition-type': 'cooking',
            #'category[0]': 'generic-foods',
            #'health[0]': 'alcohol-free',
        }
        headers = {
            'X-RapidAPI-Key': '5aaf062d7fmshdb5be57df4740b2p193729jsn5b260789ab0e',
            'X-RapidAPI-Host': 'edamam-food-and-grocery-database.p.rapidapi.com'
        }
        if request.method == 'GET' and 'q' in request.GET:
            params['ingr'] = request.GET.get('q')
            response = requests\
                .get('https://edamam-food-and-grocery-database.p.rapidapi.com/api/food-database/v2/parser',
                     params=params, headers=headers)
            data = response.json()
            print(data['text'])
            print(data['parsed'])
        else:
            data = {}

        return JsonResponse(json.dumps(data['parsed']), safe=False)


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

    def get_queryset(self):
        list_of_ingredients = self.request.query_params.get("ingredients", None)
        if list_of_ingredients:
            list2 = list(list_of_ingredients.lower().split(","))
            qs1 = IngredientQuantity.objects.annotate(lower_label=Lower('ingredient__label')).filter(lower_label__in=list2)
            qs = Dish.objects.filter(pk__in=qs1.all().values_list('dish_id'))
            return qs
        return super().get_queryset()


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

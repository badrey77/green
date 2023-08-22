from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UserViewSet, IngredientViewSet, RestaurantViewSet, MenuViewSet, ModeViewSet,
    DishBaseViewSet, DishViewSet, MenuItemViewSet, IngredientQuantityViewSet,
    ProfileViewSet, AdminProfileViewSet, CustomerProfileViewSet, ManagerProfileViewSet,
    OrderViewSet, TagViewSet, SocialAccountViewSet, OrderedDishViewSet
)

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'ingredients', IngredientViewSet)
router.register(r'restaurants', RestaurantViewSet)
router.register(r'menus', MenuViewSet)
router.register(r'modes', ModeViewSet)
router.register(r'dishbases', DishBaseViewSet)
router.register(r'dishes', DishViewSet)
router.register(r'menuitems', MenuItemViewSet)
router.register(r'ingredientquantities', IngredientQuantityViewSet)
router.register(r'profiles', ProfileViewSet)
router.register(r'adminprofiles', AdminProfileViewSet)
router.register(r'customerprofiles', CustomerProfileViewSet)
router.register(r'managerprofiles', ManagerProfileViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'tags', TagViewSet)
router.register(r'socialaccounts', SocialAccountViewSet)
router.register(r'ordereddishes', OrderedDishViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

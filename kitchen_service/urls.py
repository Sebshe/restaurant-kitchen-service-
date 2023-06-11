from django.urls import path

from .views import (
    MainView,
    DishTypeListView,
    DishTypeCreateView
)

urlpatterns = [
    path('', MainView.as_view(), name='index'),
    path(
        'types_of_dish/',
        DishTypeListView.as_view(),
        name='types-of-dish'
    ),
    path(
        'types_of_dish/create/',
        DishTypeCreateView.as_view(),
        name='types-of-dish-create'
    ),
]

app_name = "kitchen_service"

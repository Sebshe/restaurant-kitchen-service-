from django.urls import path

from .views import (
    MainView,
    DishTypeListView,
    DishTypeCreateView,
    DishTypeDetailView,
    DishTypeUpdateView,
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
    path(
        'types_of_dish/<int:pk>/',
        DishTypeDetailView.as_view(),
        name="type-of-dish-detail"
    ),
    path(
        'types_of_dish/<int:pk>/update/',
        DishTypeUpdateView.as_view(),
        name='type-of-dish-update'
    ),
]

app_name = "kitchen_service"

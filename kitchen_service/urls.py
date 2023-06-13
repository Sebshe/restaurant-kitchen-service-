from django.urls import path

from .views import (
    MainView,
    DishTypeListView,
    DishTypeCreateView,
    DishTypeDetailView,
    DishTypeUpdateView,
    DishTypeDeleteView,
    CookListView,
    CookDetailView,
    CookUpdateView,
    DishListView,
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
    path(
        "types_of_dish/<int:pk>/delete/",
        DishTypeDeleteView.as_view(),
        name="type-of-dish-delete"
    ),
    path(
        'cooks/',
        CookListView.as_view(),
        name='cooks'
    ),
    path(
        'cooks/<int:pk>/',
        CookDetailView.as_view(),
        name="cook-detail"
    ),
    path(
        'cooks/<int:pk>/update/',
        CookUpdateView.as_view(),
        name='cook-update'
    ),
    path(
        'dishes/',
        DishListView.as_view(),
        name='dishes',
    )
]

app_name = "kitchen_service"

from django.urls import path

from .views import MainView, DishTypeListView

urlpatterns = [
    path('', MainView.as_view(), name='index'),
    path(
        'types_of_dish/',
        DishTypeListView.as_view(),
        name='types-of-dish'
    ),
]

app_name = "kitchen_service"

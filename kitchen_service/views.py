from typing import Optional

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView

from kitchen_service.forms import DishTypeSearchForm
from kitchen_service.models import DishType, Dish, Cook


class MainView(TemplateView):
    template_name = 'kitchen_service/index.html'

    def get_context_data(self, **kwargs):
        context = super(MainView, self).get_context_data(**kwargs)
        context['dish_types_count'] = DishType.objects.count()
        context['dishes_count'] = Dish.objects.count()
        context['cooks_count'] = Cook.objects.count()
        return context


class DishTypeListView(LoginRequiredMixin, ListView):
    model = DishType
    template_name = 'kitchen_service/dish_type_list.html'

    def get_context_data(self, *, object_list: Optional[list] = None, **kwargs):
        context = super(DishTypeListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name", "")
        context['search_form'] = DishTypeSearchForm(
            initial={
                "name": name
            }
        )
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.GET.get("name")
        if name:
            queryset = queryset.filter(name__icontains=name)
        return queryset

from django.views.generic import TemplateView

from kitchen_service.models import DishType, Dish, Cook


class MainView(TemplateView):
    template_name = 'kitchen_service/index.html'

    def get_context_data(self, **kwargs):
        context = super(MainView, self).get_context_data(**kwargs)
        context['dish_types_count'] = DishType.objects.count()
        context['dishes_count'] = Dish.objects.count()
        context['cooks_count'] = Cook.objects.count()
        return context

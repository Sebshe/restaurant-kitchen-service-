from typing import Optional, Any

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import (
    TemplateView,
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
)

from kitchen_service.forms import (
    DishTypeSearchForm,
    DishTypeForm,
    CookSearchForm,
    CookUpdateForm,
    DishSearchForm,
    DishForm
)
from kitchen_service.models import (
    DishType,
    Dish,
    Cook
)


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

    def get_context_data(
            self,
            *,
            object_list: Optional[list] = None,
            **kwargs
    ):
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


class DishTypeCreateView(LoginRequiredMixin, CreateView):
    model = DishType
    template_name = 'kitchen_service/dish_type_form.html'
    form_class = DishTypeForm
    success_url = reverse_lazy('kitchen_service:types-of-dish')


class DishTypeDetailView(LoginRequiredMixin, DetailView):
    model = DishType
    template_name = 'kitchen_service/dish_type_detail.html'


class DishTypeUpdateView(LoginRequiredMixin, UpdateView):
    model = DishType
    template_name = 'kitchen_service/dish_type_form.html'
    form_class = DishTypeForm

    def form_valid(self, form: DishTypeForm) -> HttpResponseRedirect:
        instance = form.save(commit=False)
        instance.save()
        form.save()
        return HttpResponseRedirect(instance.get_absolute_url())


class DishTypeDeleteView(LoginRequiredMixin, DeleteView):
    model = DishType
    template_name = 'kitchen_service/dish_type_confirm_delete.html'
    success_url = reverse_lazy('kitchen_service:types-of-dish')


class CookListView(LoginRequiredMixin, ListView):
    model = Cook
    template_name = 'kitchen_service/cook_list.html'

    def get_queryset(self):
        query = self.request.GET.get('search')
        if query:
            queryset = Cook.objects.filter(
                Q(first_name__icontains=query)
                | Q(last_name__icontains=query)
                | Q(username__icontains=query)
            )
        else:
            queryset = Cook.objects.all()
        return queryset

    def get_context_data(
            self,
            *,
            object_list: Optional[list] = None,
            **kwargs
    ) -> dict[str, Any]:
        context = super(CookListView, self).get_context_data(**kwargs)
        search_form = CookSearchForm(self.request.GET or None)
        if search_form.is_valid():
            cooks = search_form.search_cooks()
            context['cooks'] = cooks
        context['search_form'] = search_form
        return context


class CookDetailView(LoginRequiredMixin, DetailView):
    model = Cook
    template_name = 'kitchen_service/cook_detail.html'


class CookUpdateView(LoginRequiredMixin, UpdateView):
    model = Cook
    template_name = 'kitchen_service/cook_update_form.html'
    form_class = CookUpdateForm

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.save()
        form.save()
        return HttpResponseRedirect(instance.get_absolute_url())


class DishListView(LoginRequiredMixin, ListView):
    model = Dish
    template_name = 'kitchen_service/dish_list.html'

    def get_context_data(
            self,
            *,
            object_list: Optional[list] = None,
            **kwargs
    ):
        context = super(
            DishListView, self
        ).get_context_data(**kwargs)
        name = self.request.GET.get("name", "")
        context['search_form'] = DishSearchForm(
            initial={
                "name": name
            }
        )
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.GET.get("name")
        if name:
            queryset = queryset.filter(
                name__icontains=name
            )
        return queryset


class DishCreateView(LoginRequiredMixin, CreateView):
    model = Dish
    template_name = 'kitchen_service/dish_form.html'
    form_class = DishForm
    success_url = reverse_lazy('kitchen_service:dishes')


class DishUpdateView(LoginRequiredMixin, UpdateView):
    model = Dish
    template_name = 'kitchen_service/dish_form.html'
    form_class = DishForm

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.save()
        form.save()
        return HttpResponseRedirect(instance.get_absolute_url())

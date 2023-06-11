from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class DishType(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(
        upload_to='types_of_dish',
        blank=True,
        null=True
    )

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse(
            'kitchen_service:type-of-dish-detail',
            args=[str(self.id)]
        )

    class Meta:
        verbose_name = "type of dish"
        verbose_name_plural = "types of dish"
        ordering = ['name']


class Cook(AbstractUser):
    years_of_experience = models.PositiveIntegerField(null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='avatar', blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name} ({self.username})"

    # template for get_absolute_url
    # def get_absolute_url(self):
    #    return reverse('kitchen_service:cook-detail', args=[str(self.id)])

    class Meta:
        ordering = ['username']


class Dish(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    dish_type = models.ForeignKey(DishType, on_delete=models.CASCADE, related_name='dishes')
    cooks = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='dishes')
    image = models.ImageField(upload_to='dish', blank=True, null=True)

    def __str__(self) -> str:
        return self.name

    # template for get_absolute_url
    # def get_absolute_url(self):
    #    return reverse('kitchen_service:dish-detail', args=[str(self.id)])

    class Meta:
        verbose_name_plural = "dishes"
        ordering = ['name']

import django_filters

from restaurant.models import *


class OrderFilter(django_filters.FilterSet):

    class Meta:
        model = Order
        fields = ('client', 'paid')


class CookRequestFilter(django_filters.FilterSet):

    class Meta:
        model = CookRequest
        fields = ('food', 'cooker')

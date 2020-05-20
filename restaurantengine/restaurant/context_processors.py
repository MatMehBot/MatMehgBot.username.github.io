from itertools import count

from restaurant.models import *


def global_vars(request):
    role = Role.objects.filter(title = 'cook')

    total_users = Profile.objects.all()
    total_cookers = Profile.objects.filter(role=role[0])

    return {
        'total_users': len(total_users),
        'total_cookers': len(total_cookers),
    }
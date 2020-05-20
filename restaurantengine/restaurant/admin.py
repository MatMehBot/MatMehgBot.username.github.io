from django.contrib import admin

# Register your models here.
from restaurant.models import *

admin.site.register(Profile)
admin.site.register(Role)
admin.site.register(Food)
admin.site.register(Order)
admin.site.register(CookRequest)
admin.site.register(SupportRequest)
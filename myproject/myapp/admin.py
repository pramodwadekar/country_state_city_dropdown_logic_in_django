from django.contrib import admin
from .models import *
# Register your models

admin.site.register(student)
admin.site.register(Country)
admin.site.register(State)
admin.site.register(City)
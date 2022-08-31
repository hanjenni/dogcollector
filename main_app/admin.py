from django.contrib import admin

# Register your models here.
from .models import Dog, Feeding
admin.site.register(Dog)
admin.site.register(Feeding)
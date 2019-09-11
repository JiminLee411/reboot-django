from django.contrib import admin

# Register your models here.
from .models import PastLife

class PastLifeAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'myjob')

admin.site.register(PastLife, PastLifeAdmin)

from django.contrib import admin

# Register your models here.
from .models import Query


@admin.register(Query)
class Query(admin.ModelAdmin):
    pass

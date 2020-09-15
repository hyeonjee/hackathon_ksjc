from django.contrib import admin
from .models import Content
# Register your models here.
@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'members',
        'place',
        'doing',
        'kinds',
        'created_at',
        'updated_at',
    )
    search_fields = (
        'members',
        'place',
        'doing',
        'kinds'
    )
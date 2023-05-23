from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from simple_history.admin import SimpleHistoryAdmin

from .models import Product, Manufacturer, Category


@admin.register(Product)
class ProductAdmin(SimpleHistoryAdmin, ImportExportModelAdmin):
    list_display = ('name', 'description', 'color')
    list_filter = ('name', 'color')
    fieldsets = (
        ('Основная информация', {
            'fields': ('name', 'description', 'color')
        }),
        ('Дополнительная информация', {
            'fields': ('manufacturer', 'category')
        }),
    )

    class Meta:
        proxy = True


class ProductInline(admin.TabularInline):
    model = Product


@admin.register(Manufacturer)
class ManufacturerAdmin(SimpleHistoryAdmin, ImportExportModelAdmin):
    inlines = [ProductInline]

    class Meta:
        proxy = True


@admin.register(Category)
class CategoryAdmin(SimpleHistoryAdmin, ImportExportModelAdmin):
    class Meta:
        proxy = True

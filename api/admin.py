from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from import_export.admin import ImportExportModelAdmin
from .models import Product, Manufacturer, Category


@admin.register(Product)
class ProductAdmin(SimpleHistoryAdmin, ImportExportModelAdmin):
    class Meta:
        proxy = True


@admin.register(Manufacturer)
class ManufacturerAdmin(SimpleHistoryAdmin, ImportExportModelAdmin):
    class Meta:
        proxy = True


@admin.register(Category)
class CategoryAdmin(SimpleHistoryAdmin, ImportExportModelAdmin):
    class Meta:
        proxy = True

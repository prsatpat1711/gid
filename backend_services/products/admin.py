from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from gid.settings import SHOW_ADMIN_VIEW

from .models import Product

if SHOW_ADMIN_VIEW == True:
    class ProductAdmin(SimpleHistoryAdmin):
        list_display = (
            'id',
            'title',
            'created_by',
            'updated_by',
            'date_created',
            'last_modified',
        )
        '''
        Moved to SimpleHistory Code
        '''
        history_list_display = ["full_name", "id"]
        search_fields = ['full_name', "id"]

    admin.site.register(Product, ProductAdmin)
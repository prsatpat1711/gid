from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from gid.settings import SHOW_ADMIN_VIEW

from .models import Profile

if SHOW_ADMIN_VIEW == True:
    class ProfileAdmin(SimpleHistoryAdmin):
        list_display = (
            'id',
            'full_name',
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

    admin.site.register(Profile, ProfileAdmin)
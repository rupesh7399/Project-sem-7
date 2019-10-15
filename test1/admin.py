from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin
from import_export.admin import ImportExportModelAdmin
from .models import weather_data
from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy

@admin.register(weather_data)
class ViewAdmin(ImportExportModelAdmin):
    pass
class AapAdminSite(AdminSite):
    # the text to put at the top pf each admin page, as an <h1>
    site_header = ugettext_lazy('Anand Agricultural Planing')
    
    # Text to put at each page's <title>
    site_title = ugettext_lazy('AAP')

    # Text to put at the top of the admin index page.
    index_title = ugettext_lazy('AAP')

aap_admin_site = AapAdminSite()

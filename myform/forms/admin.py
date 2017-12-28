from django.contrib import admin
from forms.models import Entry

# Register your models here.
#from .models import Entry

#admin.site.register(Entry)

class EntryAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'address',)
#    list_display_links = ('id',)
admin.site.register(Entry, EntryAdmin)
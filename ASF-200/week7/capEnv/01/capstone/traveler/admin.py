from django.contrib import admin
from traveler.models import Location
# Register your models here.

class TravelerAdmin(admin.ModelAdmin): 
    list_display=("text", "created_on", "total_likes")
    list_filter = ['created_on']
    search_fields = ['text']

admin.site.register(Location, TravelerAdmin)


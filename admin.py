from django.contrib import admin
from .models import Contact
# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    clist=['Name','Email','Subject','message']
admin.site.register(Contact,ContactAdmin)

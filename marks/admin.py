from django.contrib import admin
from marks.models import Mark

class MarkAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ["name"]

admin.site.register(Mark, MarkAdmin)

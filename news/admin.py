from django.contrib import admin
from .models import News

# Register your models here.


class NewsAdmin(admin.ModelAdmin):
    readonly_fields = ('mod_time', 'add_time',)

admin.site.register(News, NewsAdmin)
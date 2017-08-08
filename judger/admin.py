from django.contrib import admin
from django import forms
from .models import Judger

from markdownx.fields import MarkdownxFormField
from markdownx.admin import MarkdownxModelAdmin
# Register your models here.


class JudgerModelForm(forms.ModelForm):
    description = MarkdownxFormField()

    class Meta:
        fields = '__all__'
        model = Judger


class JudgerAdmin(admin.ModelAdmin):
    form = JudgerModelForm


admin.site.register(Judger, MarkdownxModelAdmin)
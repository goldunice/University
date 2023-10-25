from django.contrib import admin
from .models import *


# admin.site.register(Major)
# admin.site.register(Subject)
# admin.site.register(Teacher)

@admin.register(Major)
class MajorForm(admin.ModelAdmin):
    list_display = ["id", "name", "active"]
    list_display_links = ["id", "name"]
    list_editable = ["active"]
    list_filter = ["active"]
    search_fields = ["name"]
    search_help_text = "Look for by name"
    list_per_page = 10


# Fanni asosiyligiga, yo’nalishiga qarab filterlash, nomi bo’yicha qidirish imkoniyatlari bo’lsin.

@admin.register(Subject)
class SubjectForm(admin.ModelAdmin):
    list_display = ["id", "name", "major", "main"]
    list_filter = ["main", "major"]
    search_fields = ["name"]


@admin.register(Teacher)
class TeacherForm(admin.ModelAdmin):
    list_display = ["id", "name", "gender", "level", "age", "subject"]
    search_fields = ["name"]




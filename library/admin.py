from django.contrib import admin
from .models import Book

# Регистрируем нашу модель
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "year")

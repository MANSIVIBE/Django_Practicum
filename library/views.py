from django.shortcuts import render
from django.views.generic import DetailView,ListView
from .models import Book


# Для вывода нашей страницы создаем класс на основе ListView
class LibraryView(ListView):
    # указываем с какой моделью будем работать
    model = Book
    # какой шаблон отобразим
    template_name = 'main/index.html'
    # контекстное имя для работы в шаблоне
    context_object_name = 'books'

    # переопределяем метод для передачи данных в шаблон
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная'

        return context
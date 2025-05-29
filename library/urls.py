
from django.urls import path
from .views import LibraryView

# имя приложения для работы с namespace
app_name = 'library'

urlpatterns = [
    # указываем наш созданный view в urls.py
    path('',LibraryView.as_view(),name='index')
]
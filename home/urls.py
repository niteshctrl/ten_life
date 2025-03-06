from django.urls import path
from .views import homepage, book, cancel

urlpatterns = [
    path('', homepage, name='homepage'),
    path('book/', book, name='book'),
    path('cancel/', cancel, name='cancel')
]
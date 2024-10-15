from django.urls import path
from .views import books_list, welcome, token_obtain_simulated

urlpatterns = [
    path('', welcome, name='home'),
    path('api/books/', books_list, name='books_list'),
    #path('api/token/', token_obtain_simulated, name='token_obtain_simulated'),
]
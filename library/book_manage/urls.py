from django.urls import path
from book_manage.views import display


urlpatterns=[
    path('display',display),
]
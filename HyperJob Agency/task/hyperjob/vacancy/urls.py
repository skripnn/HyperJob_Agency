from django.urls import path
from .views import *

urlpatterns = [
    path('', AllVacancy.as_view()),
    path('new', Create.as_view())
]
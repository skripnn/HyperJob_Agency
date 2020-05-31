from django.db import models
from django.contrib.auth.models import User


class Vacancy(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=1024)

    class Meta:
        db_table = 'vacancy_vacancy'

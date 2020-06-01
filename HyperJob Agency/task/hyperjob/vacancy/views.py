from django.shortcuts import render
from django.views import View
from .models import Vacancy


class AllVacancy(View):
    def get(self, request):
        context = {'vacancies': Vacancy.objects.all()}
        return render(request, 'vacancy/all_vacancy.html', context=context)

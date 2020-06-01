from django.shortcuts import render
from django.views import View
from .models import Resume


class AllResumes(View):
    def get(self, request):
        context = {'resumes': Resume.objects.all()}
        return render(request, 'resume/all_resumes.html', context=context)

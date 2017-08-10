from django.shortcuts import render, get_object_or_404
from .models import Problem
# Create your views here.


def problem_list(request):
    problems = Problem.objects.all()
    return render(request, 'problem_list.html', {'problems' : problems})


def problem_detail(request, problem_id):
    problem = get_object_or_404(Problem, problem_id=problem_id)
    return render(request, 'problem_detail.html', {'problem' : problem})
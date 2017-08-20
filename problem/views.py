from django.shortcuts import render, get_object_or_404
from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Problem
# Create your views here.


def problem_list(request):
    per_page = settings.PROBLEMS_PER_PAGE

    problem_set = Problem.objects.all()
    paginator = Paginator(problem_set, per_page)
    page = request.GET.get('page')
    try:
        problems = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        problems = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        problems = paginator.page(paginator.num_pages)

    return render(request, 'problem_list.html', {'problems': problems})


def problem_detail(request, problem_id):
    problem = get_object_or_404(Problem, problem_id=problem_id)
    return render(request, 'problem_detail.html', {'problem' : problem})
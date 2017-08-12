from django.shortcuts import render, get_object_or_404
from .models import Submission
# Create your views here.


def submission_list(request):
    submissions = Submission.objects.all()
    return render(request, 'submission_list.html', {'submissions':submissions})


def submission_detail(request, submission_id):
    submission = get_object_or_404(Submission, pk=submission_id)
    return render(request, 'submission_detail.html', {'submission':submission})

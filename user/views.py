from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def profile(request):
    user = request.user
    return render(request, 'profile.html', {'user' : user})

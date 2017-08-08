from django.shortcuts import HttpResponse, render
from django.http import Http404
from .models import News
# Create your views here.


def index(request):
    return HttpResponse('news index')


def detail(request, news_id):
    try:
        news = News.objects.get(id = str(news_id))
    except News.DoesNotExist:
        raise Http404
    return HttpResponse('news id: {0}'.format(news_id))


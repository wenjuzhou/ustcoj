from django.shortcuts import HttpResponse, render
from django.shortcuts import get_object_or_404
from .models import News
# Create your views here.


def index(request):
    news_list = News.objects.all()
    return render(request, 'news_list.html', {'news_list' : news_list})


def detail(request, news_id):
    news = get_object_or_404(News, pk=str(news_id))
    return render(request, 'news_detail.html', {'news': news})


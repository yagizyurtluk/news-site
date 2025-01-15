from django.shortcuts import render
from .models import News

def index(request):
    latest_news_list = News.objects.order_by('-pub_date')[:5]
    context = {'latest_news_list': latest_news_list}
    return render(request, 'news/index.html', context)

def detail(request, news_id):
    news = News.objects.get(pk=news_id)
    return render(request, 'news/detail.html', {'news': news})

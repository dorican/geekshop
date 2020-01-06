from django.shortcuts import render
from newsapp.models import News


def index(request):
    all_news = News.objects.all().order_by('-created')
    context = {
        'page_title': 'новости компании',
        'all_news': all_news,
    }
    return render(request, 'newsapp/index.html', context)


def news(request, slug):
    new_detail = News.objects.filter(slug=slug)
    context = {
        'new_detail': new_detail,
    }
    return render(request, "newsapp/new.html", context)
from django.shortcuts import render
from django.http import HttpResponse
from .models import Article

app_name ='news'
# Create your views here.
def index(request):
    return HttpResponse('hello index news')

def year_archive(request, year):
    a_list = Article.objects.filter(pub_date__year=year)
    context = {'year': year, 'article_list': a_list}
    return render(request, 'news/year_archive.html', context)
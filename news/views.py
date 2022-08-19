from django.shortcuts import render

# Create your views here.
from .models import Article


def year_archive(request, year):
    """
    按年归档
    """
    # a_list = Article.objects.filter(pub_date__year=year).prefetch_related('reporter')
    # a_list = Article.objects.filter(pub_date__year=year)
    a_list = Article.objects.filter(pub_date__year=year).select_related("reporter")
    context = {'year': year, 'article_list': a_list}
    return render(request, 'news/year_archive.html', context=context)


def month_archive(request):
    """
    按每年的月份归档
    """
    return None


def article_detail(request):
    """
    文章详情
    """
    return None

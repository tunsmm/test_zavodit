from django.db.models import Sum
from django.shortcuts import get_object_or_404, render
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from taggit.models import Tag

from .forms import NewsForm
from .models import News


def index(request):
    return render(request, 'index.html')


class AllNewsListView(ListView):
    queryset = News.objects.all()
    context_object_name = 'all_news'
    template_name = 'list.html'


class NewsDetailView(DetailView):
    model = News
    context_object_name = 'news'
    template_name = "detail.html"


class NewsDeleteView(DeleteView):
    model = News
    context_object_name = 'news'
    success_url = "/news"
    template_name = "delete.html"


class NewsUpdateView(UpdateView):
    model = News
    template_name = "new.html"
    form_class = NewsForm


class NewsCreateView(CreateView):
    model = News
    template_name = "new.html"
    form_class = NewsForm


def all_news_by_tag(request, search_tag=None):
    news_list = News.objects.all()
    filter_tag = None

    if search_tag:
        filter_tag = get_object_or_404(Tag, slug=search_tag)
        news_list = news_list.filter(tags__in=[filter_tag])
    
    return render(request, 'list.html', {'all_news': news_list})

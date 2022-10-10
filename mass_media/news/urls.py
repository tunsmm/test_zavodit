from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('news', views.AllNewsListView.as_view(), name='all-news'),
    
    path('news/new', views.NewsCreateView.as_view(), name='news-new'),
    path('news/<int:pk>', views.NewsDetailView.as_view(), name='news-detail'),
    path('news/<int:pk>/update', views.NewsUpdateView.as_view(), name='news-update'),
    path('news/<int:pk>/delete', views.NewsDeleteView.as_view(), name='news-delete'),
    
    path('news/<slug:search_tag>', views.all_news_by_tag, name='news-by-tag'),
]

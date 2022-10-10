from django.urls import include, path
from rest_framework.routers import DefaultRouter, SimpleRouter

from .views import NewsViewSet


router = SimpleRouter()
# router = DefaultRouter()

router.register(r'news', NewsViewSet)
# router.register('news', NewsViewSet, basename='news')
# router.register('news/<int:pk>', NewsViewSet.as_view({'delete': 'destroy'}), basename='news-change')


urlpatterns = [
    path('v1/', include(router.urls)),
]

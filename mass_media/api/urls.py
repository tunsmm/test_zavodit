from django.urls import include, path
from rest_framework.routers import SimpleRouter

from .views import NewsViewSet


router = SimpleRouter()

router.register(r'news', NewsViewSet)

urlpatterns = [
    path('v1/', include(router.urls)),
]

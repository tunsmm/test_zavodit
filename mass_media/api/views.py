from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt


from news.models import News
from .permissions import IsAuthorOrReadOnly
from .serializers import NewsSerializer

"""
class NewsViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = News.objects.all()
        serializer = NewsSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = News.objects.filter(pk=pk)
        News = get_object_or_404(queryset)
        serializer = NewsSerializer(News)
        return Response(serializer.data)

    def create(self, request):
        serializer = NewsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'news created'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        pass
"""

class NewsViewSet(ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


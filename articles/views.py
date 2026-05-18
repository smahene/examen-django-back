from rest_framework import generics
from .models import Article
from .serializers import ArticleSerializer
from django.http import JsonResponse

class ArticleListView(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

def health_check(request):
    return JsonResponse({"status": "ok", "message": "API is healthy"})

def trigger_error(request):
    division_by_zero = 1 / 0
    return JsonResponse({"this": "will never be returned"})
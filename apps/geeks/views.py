from rest_framework import viewsets, mixins # type: ignore
from .models import Recipe
from .serializers import RecipeSerializer

class RecipeViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


    from rest_framework.pagination import PageNumberPagination

class CustomPagination(PageNumberPagination): # type: ignore
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100
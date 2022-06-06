from rest_framework.viewsets import ModelViewSet
from django.db.models import Q
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_201_CREATED
import django_filters.rest_framework
from .models import Product, Category, Manufacturer
from .serializers import ProductSerializer, CategorySerializer, ManufacturerSerializer


class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.filter(Q(color='WHITE') | Q(color='RED'))
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['manufacturer', 'color']


class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class ManufacturerViewSet(ModelViewSet):
    serializer_class = ManufacturerSerializer
    queryset = Manufacturer.objects.all()

    def create(self, request):
        fields = ['name', 'description', 'country']

        for field in fields:
            if field not in request.data:
                return Response({'message': f'field {field} must not be empty'}, status=HTTP_400_BAD_REQUEST)

        new = Manufacturer.objects.create(
            name=request.data['name'],
            description=request.data['description'],
            country=request.data['country']
        )
        new.save()
        return Response({'message': 'done'}, status=HTTP_201_CREATED)
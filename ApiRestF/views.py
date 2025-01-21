# Create your views here.

from rest_framework.viewsets import ModelViewSet
from .models import Productos
from .serializers import ProductoSerializer

class ProductoViewSet(ModelViewSet):
    queryset = Productos.objects.all()
    serializer_class = ProductoSerializer

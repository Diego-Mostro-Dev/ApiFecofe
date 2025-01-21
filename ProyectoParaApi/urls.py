from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from ApiRestF.views import ProductoViewSet
from django.http import HttpResponse

router = DefaultRouter()
router.register(r'productos', ProductoViewSet)

# Función para manejar la solicitud del favicon
def favicon(request):
    return HttpResponse(status=204)  # Respuesta vacía para evitar el error 400

# Combina las rutas en una sola lista
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('favicon.ico', favicon),  # Ruta para favicon
]

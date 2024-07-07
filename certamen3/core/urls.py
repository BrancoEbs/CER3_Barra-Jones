from django.urls import path
from .views import PlantaList, ProductoList, RegistroProduccionList, RegistroProduccionDetail, home, registro_produccion, perfil, user_registros, editar_registro

app_name = 'core'

urlpatterns = [
    path('', home, name='home'),
    path('registro/', registro_produccion, name='registro_produccion'),
    path('api/plantas/', PlantaList.as_view(), name='planta-list'),
    path('api/productos/', ProductoList.as_view(), name='producto-list'),
    path('api/registros/', RegistroProduccionList.as_view(), name='registroproduccion-list'),
    path('api/registros/<int:pk>/', RegistroProduccionDetail.as_view(), name='registroproduccion-detail'),
    path('perfil/', perfil, name='perfil'),
    path('mis-registros/', user_registros, name='user_registros'),
    path('editar-registro/<int:pk>/', editar_registro, name='editar_registro'),
]

from rest_framework import generics, filters
from .serializers import PlantaSerializer, ProductoSerializer, RegistroProduccionSerializer
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Planta, Producto, RegistroProduccion
from .forms import RegistroProduccionForm
from django.db.models import Sum
from .utils import send_slack_notification

class PlantaList(generics.ListCreateAPIView):
    queryset = Planta.objects.all()
    serializer_class = PlantaSerializer

class ProductoList(generics.ListCreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class RegistroProduccionList(generics.ListCreateAPIView):
    queryset = RegistroProduccion.objects.all()
    serializer_class = RegistroProduccionSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['fecha_produccion__year', 'fecha_produccion__month']

class RegistroProduccionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = RegistroProduccion.objects.all()
    serializer_class = RegistroProduccionSerializer

def home(request):
    return render(request, 'core/home.html')

@login_required
def registro_produccion(request):
    if request.method == 'POST':
        form = RegistroProduccionForm(request.POST)
        if form.is_valid():
            try:

                registro = form.save(commit=False)
                registro.operador = request.user
                total_litros = RegistroProduccion.objects.filter(producto=registro.producto).aggregate(Sum('litros'))['litros__sum']
                if total_litros is None:
                    total_litros = 0
                registro.total_litros = total_litros + registro.litros
                registro.save()
                
                cod_planta = "PRG"  
                cod_produ = registro.pk  
                cod_combustible = registro.producto.codigo  
                litros = registro.litros
                total = registro.total_litros  

                send_slack_notification(cod_planta, cod_produ, cod_combustible, litros, total)

                return redirect('core:home')
            
            except Exception as e:
                form.add_error(None, 'Error al registrar la producción: ' + str(e))
    else:
        form = RegistroProduccionForm()
    return render(request, 'core/registro.html', {'form': form})

@login_required
def perfil(request):
    return render(request, 'core/perfil.html')

@login_required
def mis_registros(request):
    registros = RegistroProduccion.objects.filter(operador=request.user)
    return render(request, 'core/mis_registros.html', {'registros': registros})


@login_required
def editar_registro(request, pk):
    registro = get_object_or_404(RegistroProduccion, pk=pk, operador=request.user)
    if request.method == 'POST':
        form = RegistroProduccionForm(request.POST, instance=registro)
        if form.is_valid():
            form.save()
            return redirect('core:mis_registros')
    else:
        form = RegistroProduccionForm(instance=registro)
    return render(request, 'core/editar_registro.html', {'form': form, 'registro': registro})
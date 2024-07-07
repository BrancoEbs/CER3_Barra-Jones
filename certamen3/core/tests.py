from django.test import TestCase
from .models import Planta, Producto, RegistroProduccion
from django.contrib.auth import get_user_model

class RegistroProduccionTestCase(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='testuser', password='12345')
        self.planta = Planta.objects.create(codigo='PRG', nombre='Planta de Gasolina')
        self.producto = Producto.objects.create(codigo='G93', nombre='Gasolina 93 Octanos', planta=self.planta)

    def test_registro_produccion(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.post('/core/api/registros/', {
            'producto': self.producto.id,
            'litros': 1000,
            'fecha_produccion': '2024-07-01',
            'turno': 'AM',
        })
        self.assertEqual(response.status_code, 201)  # Creación exitosa
        self.assertEqual(RegistroProduccion.objects.count(), 1)
        registro = RegistroProduccion.objects.first()
        self.assertEqual(registro.litros, 1000)
        self.assertEqual(registro.operador, self.user)

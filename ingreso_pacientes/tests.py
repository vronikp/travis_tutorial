from django.test import TestCase

# Create your tests here.
from ingreso_pacientes.models import Paciente

#Creando casos de prueba
class CrearPaciente(TestCase):

    def crear_paciente(self):
        self.paciente = Paciente.objects.create(nombres='Juan',apellidos='Vargas',cedula='0955555555');

    def test_crear_paciente(self):
        self.crear_paciente()
        self.assertIsInstance(self.paciente,Paciente,'paciente creado exitosamente')

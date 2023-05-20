from classes import *
import unittest, sys

# Pruebas unitarias

class TestGestionTurnos(unittest.TestCase):
    def setUp(self):
        # Configurar objetos necesarios para las pruebas
        self.punto1 = PuntoGeografico(10.1234, -75.5678)
        self.punto2 = PuntoGeografico(10.4321, -75.8765)
        self.ruta = Ruta([self.punto1, self.punto2])
        self.conductor = Persona("1234567890", "John Doe")
        self.asistente1 = Persona("9876543210", "Jane Smith")
        self.asistente2 = Persona("5432167890", "Alice Johnson")
        self.camion = Camion("ABC123", self.conductor, [self.asistente1, self.asistente2])
        self.centro_acopio = CentroAcopio()

    def test_validar_turno_asistentes_correctos(self):
        # Prueba para verificar que un turno con 2 asistentes no genere una excepción
        inicio = datetime.now()
        duracion = 4  # Duración de 4 horas
        turno = TurnoFactory.crear_turno(self.camion, self.ruta, inicio, duracion)

        try:
            turno.validar_turno()
        except ValueError:
            self.fail("Se generó una excepción inesperada.")

    def test_validar_turno_asistentes_incorrectos(self):
        # Prueba para verificar que un turno con menos de 2 asistentes genere una excepción
        inicio = datetime.now()
        duracion = 4  
        self.camion.asistentes = [self.asistente1] 
        turno = TurnoFactory.crear_turno(self.camion, self.ruta, inicio, duracion)

        with self.assertRaises(ValueError):
            turno.validar_turno()

    def test_validar_turno_horas_correctas(self):
        # Prueba para verificar que un turno con hora de finalización mayor a la hora de inicio no genere una excepción
        inicio = datetime.now()
        duracion = 4  
        turno = TurnoFactory.crear_turno(self.camion, self.ruta, inicio, duracion)

        try:
            turno.validar_turno()
        except ValueError:
            self.fail("Se generó una excepción inesperada.")

    def test_validar_turno_horas_incorrectas(self):
        # Prueba para verificar que un turno con hora de finalización igual a la hora de inicio genere una excepción
        inicio = datetime.now()
        duracion = 0 
        turno = TurnoFactory.crear_turno(self.camion, self.ruta, inicio, duracion)

        with self.assertRaises(ValueError):
            turno.validar_turno()

    def test_clasificar_carga(self):
        # Prueba para verificar que la carga se clasifique correctamente en el centro de acopio
        inicio = datetime.now()
        duracion = 4  
        turno = TurnoFactory.crear_turno(self.camion, self.ruta, inicio, duracion)

        vidrio = 2  
        papel = 1  
        plastico = 3  
        metal = 0  
        organicos = 2.5  

        self.centro_acopio.clasificar_carga(turno, vidrio, papel, plastico, metal, organicos)
        carga_clasificada = self.centro_acopio.carga_clasificada[turno]

        self.assertEqual(carga_clasificada['vidrio'], vidrio)
        self.assertEqual(carga_clasificada['papel'], papel)
        self.assertEqual(carga_clasificada['plastico'], plastico)
        self.assertEqual(carga_clasificada['metal'], metal)
        self.assertEqual(carga_clasificada['organicos'], organicos)

if __name__ == '__main__':
    unittest.main()
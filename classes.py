from datetime import datetime, timedelta
import time

class PuntoGeografico:
    def __init__(self, latitud, longitud):
        self.latitud = latitud
        self.longitud = longitud

class Ruta:
    def __init__(self, puntos_geograficos):
        self.puntos_geograficos = puntos_geograficos

class Persona:
    def __init__(self, identificacion, nombre):
        self.identificacion = identificacion
        self.nombre = nombre

class Camion:
    def __init__(self, placa, conductor, asistentes):
        self.placa = placa
        self.conductor = conductor
        self.asistentes = asistentes

class Turno:
    def __init__(self, camion, ruta, inicio, fin):
        self.camion = camion
        self.ruta = ruta
        self.inicio = inicio
        self.fin = fin

    def validar_turno(self):
        if len(self.camion.asistentes) != 2:
            raise ValueError("Deben haber 2 asistentes por camión.")
        
        if self.fin <= self.inicio:
            raise ValueError("La hora de finalización no puede ser la misma a la hora de inicio.")

class CentroAcopio:
    def __init__(self):
        self.carga_clasificada = {}

    def clasificar_carga(self, turno, vidrio, papel, plastico, metal, organicos):
        carga = {
            'vidrio': vidrio,
            'papel': papel,
            'plastico': plastico,
            'metal': metal,
            'organicos': organicos
        }
        self.carga_clasificada[turno] = carga

class TurnoFactory:
   
    # Factory Method

    @staticmethod
    def crear_turno(camion, ruta, inicio, duracion):
        fin = inicio + timedelta(hours=duracion)
        turno = Turno(camion, ruta, inicio, fin)
        return turno
    
    # Fin Factory Method
    
class GestionTurnos:

    # Singleton

    _instancia = None

    def __new__(cls):
        if not cls._instancia:
            cls._instancia = super().__new__(cls)
        return cls._instancia
   
    # Fin Singleton

    def __init__(self):
        self.turnos = []

    def agregar_turno(self, turno):
        self.turnos.append(turno)

    def mostrar_informacion_turnos(self):
        for turno in self.turnos:
            print("================================================================")
            print("|                            Turno                             |")
            print("================================================================")
            print("Placa:", turno.camion.placa)
            print("Conductor:", turno.camion.conductor.nombre)
            print("Asistentes:")
            for asistente in turno.camion.asistentes:
                print("-", asistente.nombre)
            print("Ruta:")
            for punto in turno.ruta.puntos_geograficos:
                print("- Latitud:", punto.latitud, "Longitud:", punto.longitud)
            print("Inicio:", turno.inicio)
            print("Fin:", turno.fin)
            print("Carga de basura clasificada:")
            if turno in centro_acopio.carga_clasificada:
                carga = centro_acopio.carga_clasificada[turno]
                print("- Vidrio:", carga['vidrio'], "toneladas")
                print("- Papel:", carga['papel'], "toneladas")
                print("- Plástico:", carga['plastico'], "toneladas")
                print("- Metal:", carga['metal'], "toneladas")
                print("- Orgánicos:", carga['organicos'], "toneladas")
            else:
                print("No se ha clasificado la carga de basura para este turno.")
            print("================================================================")


# Simulación de la aplicación

# Puntos por los que la ruta pasa
punto1 = PuntoGeografico(40.7128, -74.0060)
punto2 = PuntoGeografico(34.0522, -118.2437)
punto3 = PuntoGeografico(51.5074, -0.1278)
punto4 = PuntoGeografico(60.5004, -234.1313)

# Rutas en base a los puntos creados
ruta1 = Ruta([punto1, punto2])
ruta2 = Ruta([punto3, punto4])

# Personas
conductor = Persona(13142414, "Juan Angulo")
asistente1 = Persona(22412415, "Carlos Acevedo")
asistente2 = Persona(312415151, "Ana Gamarra")

# Camiones con el equipo respectivo
camion1 = Camion("CDJ 328", conductor, [asistente1, asistente2])
camion2 = Camion("XLM 791", conductor, [asistente1, asistente2])

# Crear una instancia de GestionTurnos
gestion_turnos = GestionTurnos()

# Crear turnos
inicio1 = datetime(2023, 5, 19, 8, 0)
turno1 = TurnoFactory.crear_turno(camion1, ruta1, inicio1, 8)
gestion_turnos.agregar_turno(turno1)

inicio2 = datetime(2023, 5, 20, 13, 30)
turno2 = TurnoFactory.crear_turno(camion2, ruta2, inicio2, 6)
gestion_turnos.agregar_turno(turno2)

# Crear un centro de acopio y clasificar la carga de los turnos
centro_acopio = CentroAcopio()
centro_acopio.clasificar_carga(turno1, 2, 3, 1, 4, 5)
centro_acopio.clasificar_carga(turno2, 1, 2, 3, 4, 5)

# Validar los turnos creados
try:
    turno1.validar_turno()
    print("El turno 1 es válido.")
except ValueError as e:
    print("Error en el turno 1:", str(e))

try:
    turno2.validar_turno()
    print("El turno 2 es válido.")
except ValueError as e:
    print("Error en el turno 2:", str(e))

# Mostrar la información de los turnos almacenados en la gestión de turnos
gestion_turnos.mostrar_informacion_turnos()
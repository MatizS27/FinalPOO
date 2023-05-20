from classes import *

# Prueba de rendimiento

gestion_turnos = GestionTurnos()

camion = Camion(placa="C001", conductor=Persona(identificacion=123512455, nombre="Juan"), asistentes=[
    Persona(identificacion= 211236235, nombre="Asistente1"),
    Persona(identificacion= 493252780, nombre="Asistente2")
])

ruta = Ruta(puntos_geograficos=[
    PuntoGeografico(latitud=10.123, longitud=20.456),
    PuntoGeografico(latitud=30.789, longitud=40.012),
    PuntoGeografico(latitud=50.345, longitud=60.678)
])

# Medir el tiempo de creación de turnos
tiempo_inicio = time.time()

# Crear múltiples turnos
for _ in range(10000):
    inicio = datetime.now()
    duracion = 8  # Duración de 8 horas
    turno = TurnoFactory.crear_turno(camion, ruta, inicio, duracion)
    gestion_turnos.agregar_turno(turno)

tiempo_fin = time.time()
tiempo_total = tiempo_fin - tiempo_inicio

print("Tiempo total de creación de turnos:", tiempo_total, "segundos")
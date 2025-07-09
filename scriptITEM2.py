# scriptITEM2.py
# Calcula distancia entre dos ciudades usando Geopy

from geopy.geocoders import Nominatim
from geopy.distance import geodesic

# Velocidades promedio por tipo de transporte (en km/h)
velocidades = {
    "1": 80,   # Auto
    "2": 15,   # Bicicleta
    "3": 5     # Caminando
}

geolocalizador = Nominatim(user_agent="mi-aplicacion")

print("== CALCULADORA DE DISTANCIA ENTRE CHILE Y ARGENTINA ==")
print("Escribe 's' para salir.\n")

while True:
    origen = input("Ciudad de origen en Chile (o 's' para salir): ")
    if origen.lower() == "s":
        break

    destino = input("Ciudad de destino en Argentina (o 's' para salir): ")
    if destino.lower() == "s":
        break

    print("\nSelecciona medio de transporte:")
    print("1 - Auto")
    print("2 - Bicicleta")
    print("3 - Caminando")
    tipo = input("Opción (1/2/3): ")

    if tipo not in velocidades:
        print("Opción inválida.\n")
        continue

    try:
        ubicacion_origen = geolocalizador.geocode(origen + ", Chile")
        ubicacion_destino = geolocalizador.geocode(destino + ", Argentina")

        if not ubicacion_origen or not ubicacion_destino:
            print("No se pudieron encontrar las ciudades. Intenta con otras.\n")
            continue

        coord_origen = (ubicacion_origen.latitude, ubicacion_origen.longitude)
        coord_destino = (ubicacion_destino.latitude, ubicacion_destino.longitude)

        distancia_km = geodesic(coord_origen, coord_destino).km
        distancia_millas = distancia_km / 1.609
        velocidad = velocidades[tipo]
        duracion_horas = distancia_km / velocidad

        print("\nResultado del viaje:")
        print(f"Distancia en kilómetros: {distancia_km:.2f} km")
        print(f"Distancia en millas: {distancia_millas:.2f}")
        print(f"Duración estimada: {duracion_horas:.1f} horas\n")

    except Exception as e:
        print("Ocurrió un error:", e)


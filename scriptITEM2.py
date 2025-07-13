from geopy.geocoders import Nominatim
from geopy.distance import geodesic

velocidades = {
    "1": 120,  # Auto
    "2": 15,   # Bicicleta
    "3": 5,    # A pie
    "4": 90,   # Bus
    "5": 900,  # Avion 
}

geolocalizador = Nominatim(user_agent="examen")


print("############ Calculadora de distancias de cuidades entre Chile y Argentina #################")
print("============================================================================================")

while True:
    origen = input("Ingresa el nombre de la ciudad de Chile (s para salir): ")
    if origen == "s":
        break
    destino = input("Ingresa el nombre de la cuidad de Argentina (s para salir): ")
    if destino == "s":
        break

    print("### Medios de transportes disponibles ###")
    print("1. Auto")
    print("2. Bicicleta")
    print("3. A pie")
    print("4. Bus")
    print("5. Avion")

    transporte = input("Ingresa el numero de la opcion que desea: ")

    if transporte not in velocidades:
        print("opcion invalida...")
        continue

    ubicacion_origen = geolocalizador.geocode(origen + ", Chile")
    ubicacion_destino = geolocalizador.geocode(destino + ", Argentina")


    coordenadas_origen = (ubicacion_origen.latitude, ubicacion_origen.longitude)
    coordenadas_destino = (ubicacion_destino.latitude, ubicacion_destino.longitude)

    km_distancia = geodesic(coordenadas_origen, coordenadas_destino).km
    mph_distancia = km_distancia * 0.621371
    rapidez = velocidades[transporte]
    horas_duracion = km_distancia / rapidez

    print("Resultado del viaje:")
    print(f"Distancia en kilómetros: {km_distancia} km")
    print(f"Distancia en millas: {mph_distancia}")
    print(f"Duración estimada: {horas_duracion} horas\n")

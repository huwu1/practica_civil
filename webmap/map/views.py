from django.shortcuts import render

from django.http import JsonResponse
from .models import Arcs, Nodes, Traffic

def limpiar_coordenada(valor):

    # 1. Convertir a string y eliminar todos los puntos y comas
    s = str(valor).replace('.', '').replace(',', '')
    
    n = float(s)

    # Si el número es más grande (ej: -706089069), lo dividimos por 10 
    #  hasta que encaje en el rango correcto.
    while abs(n) > 180 and n != 0:
        n /= 10.0
        
    return n

def traffic_data_api(request):
    features = []

    # PARA LOS NODOS

    nodos = Nodes.objects.all()

    for nodo in nodos:
        feature = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [limpiar_coordenada(nodo.longitud), 
                                limpiar_coordenada(nodo.latitud)]
            },
            "properties": {
                "id": nodo.id_nodo,
                "nombre": nodo.nombre,
                "interseccion": nodo.interseccion
            }

        }

        features.append(feature)



    # PARA LOS ARCOS Y PARA LOS DATOS DE TRÁFICO (van de la mano):
    
    # select_related es para optimizar y traer los nodos de una sola vez
    # ("trae" el dato foráneo altiro)
    datos = Traffic.objects.select_related('id_arco__id_nodo1', 'id_arco__id_nodo2').all()

    for dato in datos:

        arco = dato.id_arco

        # 1. Obtenemos las coordenadas de inicio y fin
        # OJO: GeoJSON usa el orden [Longitud, Latitud] (al revés de Google)
        start_coord = [limpiar_coordenada(arco.id_nodo1.longitud), limpiar_coordenada(arco.id_nodo1.latitud)]
        end_coord   = [limpiar_coordenada(arco.id_nodo2.longitud), limpiar_coordenada(arco.id_nodo2.latitud)]

        # 2. Creamos el objeto GeoJSON para este tramo
        feature = {
            "type": "Feature",
            "geometry": {
                "type": "LineString",
                "coordinates": [start_coord, end_coord]
            },
            "properties": {
                # propiedadades del archivo arcs.csv
                "id": arco.id_arco,
                "interseccion": dato.id_arco.interseccion,
                "calle_principal": arco.calle_principal,
                "sentido": arco.sentido,
                "desde": dato.id_arco.desde_interseccion,
                "hasta": dato.id_arco.hasta_interseccion,
                "largo": arco.largo,

                # propiedades del archivo traffic.csv
                "dia": dato.dia,
                "hora": str(dato.hora),
                "plan": dato.plan,
                "tiempo": dato.tiempo,
                "velocidad": dato.velocidad,
                "tiempo_entre_largo": dato.tiempo_entre_largo,
                "dca": dato.DCA,
                "nivel_congestion": dato.nivel_congestion,
                "infeccion": dato.infeccion,
            }
        }

        features.append(feature)

    # 3. Empaquetamos todo
    geojson = {
        "type": "FeatureCollection",
        "features": features
    }

    return JsonResponse(geojson)

def vista_pantalla_mapa(request):
    return render(request, 'page.html')
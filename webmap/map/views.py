from django.shortcuts import render

from django.http import JsonResponse
from .models import Arcs, Nodes

def traffic_data_api(request):
    features = []

    # PARA LOS NODOS

    nodos = Nodes.objects.all()

    for nodo in nodos:
        features.append({
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [float(nodo.longitud), float(nodo.latitud)]
            },
            "properties": {
                "id": nodo.id_nodo,
                "nombre": nodo.nombre
            }

        })   

    # PARA LOS ARCOS:
    
    # select_related es para optimizar y traer los nodos de una sola vez
    # ("trae" el dato foráneo altiro)
    arcos = Arcs.objects.select_related('id_nodo1', 'id_nodo2').all()

    for arco in arcos:
        try:
            # 1. Obtenemos las coordenadas de inicio y fin
            # OJO: GeoJSON usa el orden [Longitud, Latitud] (al revés de Google)
            start_coord = [float(arco.id_nodo1.longitud), float(arco.id_nodo1.latitud)]
            end_coord   = [float(arco.id_nodo2.longitud), float(arco.id_nodo2.latitud)]

            # 2. Creamos el objeto GeoJSON para este tramo
            feature = {
                "type": "Feature",
                "geometry": {
                    "type": "LineString", # Es una línea
                    "coordinates": [start_coord, end_coord]
                },
                "properties": {
                    "id": arco.id_arco,
                    "calle": arco.main_street,
                    # Aquí envías el dato para colorear (ej: nivel de congestión)
                    # Si no tienes el dato aún, pon un valor de prueba como 1
                    "nivel_congestion": -1  
                }
            }
            features.append(feature)

        except Exception as e:
            print(f"Error en arco {arco.id}: {e}")
            continue

    # 3. Empaquetamos todo
    geojson = {
        "type": "FeatureCollection",
        "features": features
    }

    return JsonResponse(geojson)

def vista_pantalla_mapa(request):
    return render(request, 'page.html')
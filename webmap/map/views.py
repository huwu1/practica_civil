from django.shortcuts import render

from django.http import JsonResponse
from .models import Arcs, Nodes, Traffic

def traffic_data_api(request):
    features = []

    # PARA LOS NODOS

    nodos = Nodes.objects.all()

    for nodo in nodos:
        feature = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [float(str(nodo.longitud).replace(',', '.')), 
                                float(str(nodo.latitud).replace(',', '.'))]
            },
            "properties": {
                "id": nodo.id_nodo,
                "nombre": nodo.nombre
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
        start_coord = [float(str(arco.id_nodo1.longitud).replace(',', '.')), float((str(arco.id_nodo1.latitud).replace(',', '.')))]
        end_coord   = [float(str(arco.id_nodo2.longitud).replace(',', '.')), float((str(arco.id_nodo2.latitud).replace(',', '.')))]

        # 2. Creamos el objeto GeoJSON para este tramo
        feature = {
            "type": "Feature",
            "geometry": {
                "type": "LineString",
                "coordinates": [start_coord, end_coord]
            },
            "properties": {
                "id": arco.id_arco,
                "calle_principal": arco.calle_principal,
                "sentido": arco.sentido,
                "dia": dato.dia,
                "hora": str(dato.hora),
                "plan": dato.plan,
                "tiempo": dato.tiempo,
                "velocidad": dato.velocidad,
                "tiempo_entre_largo": dato.tiempo_entre_largo,
                "dca": dato.DCA,
                "nivel_congestion": dato.nivel_congestion,
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
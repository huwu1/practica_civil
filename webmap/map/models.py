from django.db import models

# Nodos con sus coordenadas
class Nodes(models.Model):
    id_nodo = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    latitud = models.FloatField()
    longitud = models.FloatField()
    interseccion = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.id_nodo}: {self.latitud}, {self.longitud}"

# Arcos; conexiones entre dos nodos
class Arcs(models.Model): 
    id_arco = models.IntegerField(primary_key=True)
    interseccion = models.IntegerField()
    calle_principal = models.CharField(max_length=100)
    sentido = models.CharField(max_length=100)
    desde_interseccion = models.CharField(max_length=100)
    hasta_interseccion = models.CharField(max_length=100)
    id_nodo1 = models.ForeignKey(Nodes, on_delete=models.CASCADE, related_name='arcos_origen')
    id_nodo2 = models.ForeignKey(Nodes, on_delete=models.CASCADE, related_name='arcos_destino')
    largo = models.IntegerField()

    def __str__(self):
        return f"Arco de {self.id_nodo1_id} a {self.id_nodo2_id}"

# Cada arco con información relevante cada 15 minutos
class Traffic(models.Model):
    id = models.IntegerField(primary_key=True)
    calle_principal = models.CharField(max_length=100)
    dia = models.CharField(max_length=100)
    hora = models.TimeField()
    plan = models.CharField(max_length=100)
    tiempo = models.FloatField()
    velocidad = models.FloatField()
    tiempo_entre_largo = models.FloatField()
    DCA = models.FloatField()
    nivel_congestion = models.IntegerField(null=True, blank=True)
    infeccion_global_nivel_4 = models.IntegerField(null=True, blank=True)
    infeccion_global_nivel_5 = models.IntegerField(null=True, blank=True)
    infeccion_punta_tarde_nivel_4 = models.IntegerField(null=True, blank=True)
    infeccion_punta_tarde_nivel_5 = models.IntegerField(null=True, blank=True)
    infeccion_punta_mediodia_nivel_4 = models.IntegerField(null=True, blank=True)
    infeccion_punta_mediodia_nivel_5 = models.IntegerField(null=True, blank=True)
    id_arco = models.ForeignKey(Arcs, on_delete=models.CASCADE, related_name='arco_hora_x')

class Average(models.Model):
    id = models.IntegerField(primary_key=True)
    hora = models.TimeField()
    tiempo_entre_largo_promedio = models.FloatField(null=True, blank=True)
    dca_promedio = models.FloatField(null=True, blank=True)
    nivel_promedio = models.IntegerField(null=True, blank=True)
    id_arco = models.ForeignKey(Arcs, on_delete=models.CASCADE, related_name='arco_promedio_x')





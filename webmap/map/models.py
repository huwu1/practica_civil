from django.db import models

class Nodes(models.Model):
    id_nodo = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    latitud = models.FloatField()
    longitud = models.FloatField()

    def __str__(self):
        return f"{self.id_nodo}: {self.latitud}, {self.longitud}"

class Arcs(models.Model): 
    id_arco = models.IntegerField(primary_key=True)
    interseccion = models.IntegerField()
    calle_principal = models.CharField(max_length=100)
    sentido = models.CharField(max_length=100)
    desde_interseccion = models.CharField(max_length=100)
    hasta_interseccion = models.CharField(max_length=100)
    id_nodo1 = models.ForeignKey(Nodes, on_delete=models.CASCADE, related_name='arcos_origen')
    id_nodo2 = models.ForeignKey(Nodes, on_delete=models.CASCADE, related_name='arcos_destino')

    def __str__(self):
        return f"Arco de {self.id_nodo1_id} a {self.id_nodo2_id}"

class Traffic(models.Model):
    calle_principal = models.CharField(max_length=100)
    id_arco = models.ForeignKey(Arcs, on_delete=models.CASCADE, related_name='arco_hora_x')
    sentido = models.CharField(max_length=100)
    desde_interseccion = models.CharField(max_length=100)
    hasta_interseccion = models.CharField(max_length=100)
    n_interseccion = models.IntegerField()
    dia = models.CharField(max_length=100)
    hora = models.TimeField()
    plan = models.CharField(max_length=100)
    tiempo = models.FloatField()
    velocidad = models.FloatField()
    tiempo_entre_largo = models.FloatField()
    DCA = models.FloatField()
    nivel_congestion = models.IntegerField(null=True, blank=True)





from django.db import models

class Nodes(models.Model):
    id_nodo = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    latitud = models.DecimalField(max_digits=22, decimal_places=16)
    longitud = models.DecimalField(max_digits=22, decimal_places=16)

    def __str__(self):
        return f"{self.id_nodo}: {self.latitud}, {self.longitud}"

class Arcs(models.Model): 
    id_arco = models.IntegerField(primary_key=True)
    interseccion = models.IntegerField()
    main_street = models.CharField(max_length=100)
    sentido = models.CharField(max_length=100)
    from_intersection = models.CharField(max_length=100)
    to_intersection = models.CharField(max_length=100)
    id_nodo1 = models.ForeignKey(Nodes, on_delete=models.CASCADE, related_name='arcos_origen')
    id_nodo2 = models.ForeignKey(Nodes, on_delete=models.CASCADE, related_name='arcos_destino')

    def __str__(self):
        return f"Arco de {self.id_nodo1_id} a {self.id_nodo2_id}"

class DatoTrafico(models.Model):
    #interseccion = models.ForeignKey(Interseccion, related_name='datos', on_delete=models.CASCADE)
    fecha_hora = models.DateTimeField()
    velocidad = models.FloatField()
    nivel_congestion = models.IntegerField()




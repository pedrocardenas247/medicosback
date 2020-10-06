from django.db import models


class Experiencia(models.Model):
    lugar = models.CharField(max_length=150)

    def __str__(self):
        return self.lugar

    class Meta:
        verbose_name_plural = 'Experiencias'
        ordering = ['id']


class Estacionamiento(models.Model):
    nro = models.IntegerField()
    zona = models.CharField(max_length=150)

    def __str__(self):
        return "El Numero de estacionamiento es " + str(self.nro)

    class Meta:
        verbose_name_plural = 'Estacionamientos'
        ordering = ['id']


class Medico(models.Model):
    PEDIATRIA = 1
    MEDICINAGENERAL = 2
    ESTETICA = 3
    ESPECIALIDAD = (
        (PEDIATRIA, 'Pediatria'),
        (MEDICINAGENERAL, 'Medicina General'),
        (ESTETICA, 'Estetica'))
    nombre = models.CharField(max_length=150)
    apellidos = models.CharField(max_length=150)
    telefono = models.CharField(max_length=10, blank=True)
    direccion = models.CharField(max_length=150, blank=True)
    salario = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    especialidad = models.PositiveSmallIntegerField(choices=ESPECIALIDAD)
    experiencia = models.ManyToManyField(Experiencia, blank=True, null=True)
    estacionamiento = models.ForeignKey(Estacionamiento, on_delete=models.CASCADE, blank=True, null=True)
    foto = models.ImageField(upload_to='medicos/img/', blank=True, null=True, default="medicos/sinfoto.jpg")

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = 'Medicos'
        ordering = ['id']

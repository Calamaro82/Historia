from django.db import models


class Ubicacion(models.Model):
    nombre = models.CharField(max_length = 100, blank = True, null = True)
    creacion = models.DateTimeField(blank = True, null = True)
    desaparicion = models.DateTimeField(blank = True, null = True)


class Individuo(models.Model):
    nombre = models.TextField(blank = True, null = True)
    apellido = models.TextField(blank = True, null = True)
    alias = models.TextField(blank = True, null = True)
    descripcion = models.TextField(blank = True, null = True)
    imagen = models.TextField(blank = True, null = True)
    creacion = models.DateTimeField(blank = True, null = True)
    desaparicion = models.DateTimeField(blank = True, null = True)

    def __str__(self):
    	if self.alias != "":
            return "%s %s (%s)" % (self.nombre, self.apellido, self.alias)
    	else:
    		return "%s %s" % (self.nombre, self.apellido)


class Documento(models.Model):
    TIPO_DE_DOCUMENTOS = [
        ('LB', 'Libro'),
        ('VD', 'Video'),
        ('OT', 'Otro'),
    ]

    titulo = models.CharField(max_length = 100, blank = True, null = True)
    autores = models.ManyToManyField(Individuo)
    tipo = models.CharField(max_length = 2, choices = TIPO_DE_DOCUMENTOS, null = True)
    descripcion = models.TextField(blank = True, null = True)
    creacion = models.DateTimeField(blank = True, null = True)

    def __str__(self):
        autorString = []
        for autor in self.autores.all():
            autorString.append(str(autor))
        return "%s (%s)" % (self.titulo, ", ".join(autorString))


class Evento(models.Model):
    titulo = models.TextField()
    descripcion = models.TextField(blank = True, null = True)
    imagen = models.TextField(blank = True, null = True)
    fecha = models.DateTimeField(blank = True, null = True)
    individuos = models.ManyToManyField(Individuo)
    documentos = models.ManyToManyField(Documento, through = 'Fuente', through_fields = ('evento', 'documento'))
    lugar = models.OneToOneField(Ubicacion, on_delete = models.CASCADE, blank = True, null = True)

    def __str__(self):
        return "%s" % self.titulo


class Fuente(models.Model):
    documento = models.ForeignKey(Documento, on_delete = models.CASCADE)
    evento = models.ForeignKey(Evento, on_delete = models.CASCADE)
    ubicacion = models.CharField(max_length = 100)

    def __str__(self):
        return "%s - %s" % (str(self.documento), self.ubicacion)
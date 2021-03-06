from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Individuo, Fuente, Evento
from datetime import date


def index(request):
	individuosEnEventos = []
	for evento in Evento.objects.all():
		for individuo in evento.individuos.all():
			if individuo not in individuosEnEventos:
				individuosEnEventos.append(individuo)
	eventosDiarios = []
	for evento in Evento.objects.all():
		if evento.fecha.date() == date.today():
			eventosDiarios.append(evento)
	return render(request, 'cronicas/index.html', 
		          {'all_people' : individuosEnEventos,
		           'eventos_diarios' : eventosDiarios})


def detallesIndividuo(request, individuoId):
	people = get_object_or_404(Individuo, pk = individuoId)
	fuentes = get_list_or_404(Fuente, 
		                      evento__individuos__pk = individuoId)
	return render(request, 'cronicas/detalles.html', 
		         {'people': people, 'fuentes': fuentes })


def todosLosEventos(request):
	return render(request, 'cronicas/TodosLosEventos.html')
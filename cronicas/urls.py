from django.urls import path

from . import views


urlpatterns = [
	path('', views.index, name = 'index'),
	path('<int:individuoId>/', views.detallesIndividuo, name = 'detallesIndividuo'),
	path('TodosLosEventos/', views.todosLosEventos, name = 'todosLosEventos'),
]
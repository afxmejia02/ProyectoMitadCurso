from django.urls import path
from . import views


urlpatterns = [
    path('inicio',views.inicio, name='inicio'),
    path('data',views.data, name='data'),
    path('crear',views.crear, name='crear'),
    path('eliminar/<int:Id>', views.eliminar_persona, name='eliminar_persona'),
    path('eliminar/ciudad/<int:Id>/', views.eliminar_ciudad, name='eliminar_ciudad'),
    path('editar/persona/<int:ciudad_id>/', views.editar_persona, name='editar_persona'),
    path('editar/ciudad/<int:ciudad_id>/', views.editar_ciudad, name='editar_ciudad'),
]
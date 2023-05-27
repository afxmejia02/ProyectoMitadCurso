from django.shortcuts import render, redirect
from .models import Persona, TipoDocumento, Ciudad
from .forms import PersonaForm,  CiudadForm

# Create your views here.

def inicio(request):
    return render(request, 'inicio.html')

def data(request):
    personas = Persona.objects.all()
    ciudad = Ciudad.objects.all()
    tipodoc = TipoDocumento.objects.all()
    return render(request, 'data.html', {'personas':personas, 'ciudad':ciudad, 'tipodoc':tipodoc})

       

def crear(request):
    formularioPersona = PersonaForm(request.POST or None, request.FILES or None)
    formularioCiudad=CiudadForm(request.POST or None, request.FILES or None)
    if formularioPersona.is_valid() and formularioCiudad.is_valid():
        formularioPersona.save()
        formularioCiudad.save()
        return redirect('crear')
    return render(request, 'crear.html', {'formularioPersona': formularioPersona, 'formularioCiudad':formularioCiudad}) 


#Editar persona
def editar_persona(request, persona_id):
    persona = Persona.objects.get(Id=persona_id)
    formularioPersona = PersonaForm(request.POST or None, request.FILES or None, instance=persona)
    
    if request.method == 'POST':
        if formularioPersona.is_valid():
            formularioPersona.save()
            return redirect('editar_persona', persona_id=persona.Id)
    
    return render(request, 'editar.html', {'formularioPersona': formularioPersona})


# Editar ciudad
def editar_ciudad(request, ciudad_id):
    ciudad = Ciudad.objects.get(Id=ciudad_id)
    formularioCiudad = CiudadForm(request.POST or None, request.FILES or None, instance=ciudad)
    
    if request.method == 'POST':
        if formularioCiudad.is_valid():
            formularioCiudad.save()
            return redirect('editar_ciudad', ciudad_id=ciudad.Id)
    return render(request, 'editar.html', {'formularioCiudad': formularioCiudad})

def eliminar_persona(request, Id):
    persona = Persona.objects.get(Id=Id)
    persona.delete()
    return redirect('data')

def eliminar_ciudad(request, Id):
    ciudad = Ciudad.objects.get(Id=Id)
    ciudad.delete()
    return redirect('data')    




    
from django.http import HttpResponse
from AppFamilia.models import Familia
from django.template import Context, Template, loader
from django.shortcuts import render
# Create your views here.

def familia(self):
    
    familiar1 = Familia(nombre="Emiliano", apellido='Celleri', edad= 28, fecha_de_nacimiento = '1993-10-19')
    familiar1.save()
    familiar2 = Familia(nombre="Micaela", apellido='Celleri', edad= 30, fecha_de_nacimiento = '1991-07-11')
    familiar2.save()
    familiar3 = Familia(nombre="Julian", apellido='Celleri', edad= 20, fecha_de_nacimiento = '2002-12-05')
    familiar3.save()
    texto= f"Familiar Creado. nombre y apellido: {familiar1.nombre} {familiar1.apellido} edad: {familiar1.edad} fecha de nacimiento: {familiar1.fecha_de_nacimiento} <br/> Familiar Creado. nombre y apellido: {familiar2.nombre} {familiar2.apellido} edad: {familiar2.edad} fecha de nacimiento: {familiar2.fecha_de_nacimiento} <br/>Familiar Creado. nombre y apellido: {familiar3.nombre} {familiar3.apellido} edad: {familiar3.edad} fecha de nacimiento: {familiar3.fecha_de_nacimiento}" 
    return HttpResponse(texto)
    

def inicio(request):
    plantilla=loader.get_template('inicio.html')   #Leemos el archivo y lo guardamos en una variable


    documento=plantilla.render()

    return HttpResponse(documento)
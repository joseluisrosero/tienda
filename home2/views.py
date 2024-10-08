from django.shortcuts import render
from .forms import*
from .models import Producto

# Create your views here.

def vista_lista_producto (request):
    lista = Producto.objects.filter()
    return render(request, 'lista_producto.html',locals())

def vista_about(request):
    return render(request,'about.html')

def vista_funko(request):
    return render(request,'funko.html')

def vista_contacto(request):
    info_enviado=False
    email =""
    title =""
    text =""
    if request.method =="POSTt":
        formulario =contacto_form(request.POST)
        if formulario.is_valid():
            info_enviado=True
            email = formulario.cleamed_data['correo']
            title = formulario.cleamed_data['titulo']
            text = formulario.cleaned_data['texto']
    else: #si es metodo GET u otro metodo
        formulario= contacto_form()    
    return render(request,'contacto.html',locals())

def vista_home(request):
    return render(request, 'home.html')


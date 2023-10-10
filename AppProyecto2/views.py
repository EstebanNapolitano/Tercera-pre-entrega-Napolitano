from django.shortcuts import render, redirect
from .forms import FormularioContacto

def contacto(request):
    if request.method == 'POST':
        form = FormularioContacto(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contacto-exito')
    else:
        form = FormularioContacto()

    return render(request, 'contacto/contacto.html', {'form': form})

def contacto_exito(request):
    return render(request, 'contacto/contacto_exito.html')
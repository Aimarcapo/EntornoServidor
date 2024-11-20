from django.shortcuts import render,redirect, get_object_or_404
from .models import Ikasle,Ikasgaiak,Nota
from .forms import IkasleForm, IkasgaiakForm,NotaForm,NotaAldatuForm
 # Create your views here.
def ikasle_list(request):    
    ikasleZerrenda=Ikasle.objects.all()    
    return render(request, 'index.html', {'ikasleak':ikasleZerrenda})

def ikasle_new(request):    
    if request.method == 'POST':        
        form=IkasleForm(request.POST)       
        if form.is_valid:            
            ikasle = form.save()            
            ikasle.save()        
            return redirect('zerrenda-default')
    else:        
        form=IkasleForm()        
        return render(request, 'ikasle_new.html', {'form':form})
def ikasgaiak_list(request):    
    ikasgaiak=Ikasgaiak.objects.all()
    return render(request, 'ikasgaiak.html', {'ikasgaiak':ikasgaiak})
def ikasgaiak_new(request):    
    if request.method == 'POST':        
        form=IkasgaiakForm(request.POST)       
        if form.is_valid:            
            ikasgaiak = form.save()            
            ikasgaiak.save()        
            return redirect('ikasgaiak-default')
    else:        
        form=IkasgaiakForm()        
        return render(request, 'ikasgaiak_new.html', {'form':form}) 
def nota_list(request):    
    notak=Nota.objects.all()
    return render(request, 'nota.html', {'notak':notak})
def nota_new(request):    
    if request.method == 'POST':        
        form=NotaForm(request.POST)       
        if form.is_valid:            
            nota = form.save()            
            nota.save()        
            return redirect('nota-default')
    else:        
        form=NotaForm()        
        return render(request, 'nota_new.html', {'form':form})
def eliminar_nota(request, nota_id):
    nota = get_object_or_404(Nota, id=nota_id)  # Obtén la nota o muestra un error 404
    if request.method == 'POST':  # Si se envía el formulario de confirmación
        nota.delete()  # Elimina la nota
        return redirect('nota-default')  # Redirige a la lista de notas después de eliminar
    return render(request, 'nota_delete.html', {'nota': nota})  # Renderiza la página de confirmación 
def edit_nota(request, nota_id):
    nota = get_object_or_404(Nota, id=nota_id)  # Obtén la nota o muestra un error 404
    if request.method == 'POST':
        form = NotaForm(request.POST, instance=nota)  # Crea un formulario con la instancia de la nota
        if form.is_valid():  # Verifica si el formulario es válido
            form.save()  # Guarda los cambios en la nota
            return redirect('nota-default')  # Redirige a la lista de notas después de editar
    else:
        form = NotaForm(instance=nota)  # Carga el formulario con los datos actuales de la nota

    return render(request, 'nota_edit.html', {'form': form, 'nota': nota})
def editar_nota(request, ikasgai_kodea, ikasle_kodea):
    # Obtener la instancia de Nota con los códigos de materia y estudiante
    nota = get_object_or_404(Nota, ikasgai_kodea_id=ikasgai_kodea, ikasle_kodea_id=ikasle_kodea)
    
    if request.method == 'POST':
        # Cargar el formulario con los datos del POST
        form = NotaAldatuForm(request.POST, instance=nota)
        if form.is_valid():
            form.save()
            return redirect('nota-default')  # Cambiar por la vista adecuada
    else:
        # Cargar el formulario con los datos actuales de la nota
        form = NotaAldatuForm(instance=nota)

    return render(request, 'nota_edit.html', {'form': form, 'nota': nota})




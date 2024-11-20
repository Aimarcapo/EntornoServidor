from django.shortcuts import render,redirect, get_object_or_404
from .models import Kotxe,Pertsona
from .forms import KotxeForm,PertsonaForm,AlokairuForm
def kotxe_list(request):    
    kotxeIbilgailu=Kotxe.objects.all()    
    return render(request, 'kotxe.html', {'kotxeak':kotxeIbilgailu})
def kotxe_new(request):    
    if request.method == 'POST':        
        form=KotxeForm(request.POST)       
        if form.is_valid:            
            ikasle = form.save()            
            ikasle.save()        
            return redirect('kotxe-default')
    else:        
        form=KotxeForm()        
        return render(request, 'kotxe_new.html', {'form':form})
def kotxe_delete(request):
    if request.method == 'POST':        
        form=KotxeForm(request.POST)       
        if form.is_valid:            
            kotxe = form.cleaned_data['kotxea']
            kotxe.delete()  # Elimina el coche
            return redirect('kotxe-default')
    else:        
         form = KotxeForm()      
    return render(request, 'kotxe_delete.html', {'form':form})
def edit_kotxe(request, id):
    kotxe = get_object_or_404(Kotxe, matrikula=id)  # Obtén la nota o muestra un error 404, despues del modelo ponemos el nombre del campo de ese modelo que hemos puesto en models.py en este caso matrikula y despues del igual ponemos el nombre que se va a pasar por el enlace
    if request.method == 'POST':
        form = KotxeForm(request.POST, instance=kotxe)  # Crea un formulario con la instancia de la nota
        if form.is_valid():  # Verifica si el formulario es válido
            form.save()  # Guarda los cambios en la nota
            return redirect('kotxe-default')  # Redirige a la lista de notas después de editar
    else:
        form = KotxeForm(instance=kotxe)  # Carga el formulario con los datos actuales de la nota

    return render(request, 'kotxe_edit.html', {'form': form, 'kotxe': kotxe})
def pertsona_list(request):    
    pertsonaIbilgailu=Pertsona.objects.all()    
    return render(request, 'pertsona.html', {'pertsonak':pertsonaIbilgailu})
def pertsona_new(request):    
    if request.method == 'POST':        
        form=PertsonaForm(request.POST)       
        if form.is_valid:            
            ikasle = form.save()            
            ikasle.save()        
            return redirect('pertsona-default')
    else:        
        form=PertsonaForm()        
        return render(request, 'pertsona_new.html', {'form':form})
    

# Create your views here.

from django.shortcuts import render, redirect, get_object_or_404
from .models import Musician
from album.models import Album
from .forms import MusicianForm
# Create your views here.
def musician_list(request):
    musicians = Musician.objects.all() 
    albums = Album.objects.all()  # Assuming the model name is 'Album'
    context = {
        'musicians': musicians,
        'albums': albums
    }
    return render(request, 'musician_list.html', context)


def create_musician(request):
    if request.method == 'POST':
        form = MusicianForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(musician_list)
    else:
        form = MusicianForm()
    return render(request, 'musician_form.html', {'form': form})


def musician_update(request, id):
    musician = get_object_or_404(Musician, id=id)
    if request.method == 'POST':
        form = MusicianForm(request.POST, instance=musician)
        if form.is_valid():
            form.save()
            return redirect("musician_list")
    else:
        form = MusicianForm(instance=musician)
    return render(request, 'musician_form.html', {'form': form})

def musician_delete(request, id):
    musician = get_object_or_404(Musician, id=id)
    musician.delete()
    return redirect('musician_list')
from django.shortcuts import render, redirect, get_object_or_404
from .forms import AlbumForm 
from .models import Album
# Create your views here.
def create_album(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = AlbumForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('musician_list')
        else:
            form = AlbumForm()
            return render(request, 'album_form.html', {"form": form} )
    else:
        return redirect('login_page')

        
def edit_album(request, id):
    album = get_object_or_404(Album, id=id)
    if request.method == 'POST':
        form = AlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            redirect('musician_list')
    else:
        form = AlbumForm(instance=album)
    return render(request, 'album_form.html', {'form': form})
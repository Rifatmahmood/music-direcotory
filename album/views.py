from django.shortcuts import render, redirect, get_object_or_404
from .forms import AlbumForm 
from .models import Album
from django.views import View
# Create your views here.


class CreateAlbumView(View):
    def get(self, request):
        if request.user.is_authenticated:
            form = AlbumForm()
            return render(request, 'album_form.html', {'form': form})
        else:
            return redirect('login_page')

    def post(self, request):
        if request.user.is_authenticated:
            form = AlbumForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('musician_list')
            return render(request, 'album_form.html', {'form': form})
        else:
            return redirect('login_page')

class EditAlbumView(View):
    def get(self, request, id):
        album = get_object_or_404(Album, id=id)
        form = AlbumForm(instance=album)
        return render(request, 'album_form.html', {'form': form})

    def post(self, request, id):
        album = get_object_or_404(Album, id=id)
        form = AlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('musician_list')
        return render(request, 'album_form.html', {'form': form})


# def create_album(request):
#     if request.user.is_authenticated:
#         if request.method == "POST":
#             form = AlbumForm(request.POST)
#             if form.is_valid():
#                 form.save()
#                 return redirect('musician_list')
#         else:
#             form = AlbumForm()
#             return render(request, 'album_form.html', {"form": form} )
#     else:
#         return redirect('login_page')

        
# def edit_album(request, id):
#     album = get_object_or_404(Album, id=id)
#     if request.method == 'POST':
#         form = AlbumForm(request.POST, instance=album)
#         if form.is_valid():
#             form.save()
#             redirect('musician_list')
#     else:
#         form = AlbumForm(instance=album)
#     return render(request, 'album_form.html', {'form': form})
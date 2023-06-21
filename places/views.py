from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
# from .forms import PlaceForm
from .models import Place

# def create_place(request):
#     if request.method == 'POST':
#         form = PlaceForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('place_list')
#     else:
#         form = PlaceForm()
#     return render(request, 'create_place.html', {'form': form})

# def update_place(request, place_id):
#     place = get_object_or_404(Place, id=place_id)
#     if request.method == 'POST':
#         form = PlaceForm(request.POST, instance=place)
#         if form.is_valid():
#             form.save()
#             return redirect('place_list')
#     else:
#         form = PlaceForm(instance=place)
#     return render(request, 'update_place.html', {'form': form, 'place': place})

# def delete_place(request, place_id):
#     place = get_object_or_404(Place, id=place_id)
#     if request.method == 'POST':
#         place.delete()
#         return redirect('place_list')
#     return render(request, 'delete_place.html', {'place': place})

# def place_list(request):
#     places = Place.objects.all()
#     return render(request, 'place_list.html', {'places': places})



from alaapp.utils.System import System
from alaapp.models.assignment import Assignment
from django.shortcuts import redirect
from django.contrib import messages




def add_like_dislike(request):
    if System.is_logged(request):
        if System.is_player(request):   
            Assignment.objects.get(id=request.POST['assignment_id']).add_like_dislike(request.POST['assignment_bool'])
            messages.success(request,'¡Su valoración se ha guardado correctamente!')
            return redirect('see_my_game_elements')           
        return redirect('home')
    return redirect('index')

def create_scorings(request):
    if System.is_logged(request):
        if System.is_player(request): 
            Assignment.objects.get(id=request.POST['id']).add_scorings(request.POST)              
            messages.success(request,'¡Su opinión se ha guardado correctamente!')
            return redirect('see_my_game_elements')
        return redirect('home')
    return redirect('index')
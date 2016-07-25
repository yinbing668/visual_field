from django.shortcuts import render

# Create your views here.
def visualfield(request):
    return render(request, 'visualfield/visualfield.html', {})
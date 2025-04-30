from django.shortcuts import render, get_object_or_404
from .models import Hra


def index(request):
    hry = Hra.objects.all()
    return render(request, 'hry/index.html', {'hry': hry})


def detail(request, hra_id):
    hra = get_object_or_404(Hra, id=hra_id)
    return render(request, 'hry/detail.html', {'hra': hra})
from django.shortcuts import render
from django.http import HttpResponse

from .models import Zone


def index(request):
    return render(request, 'tree/tree.html')
    # return HttpResponse('you are at the tree index!')


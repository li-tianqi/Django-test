from django.shortcuts import render
from django.http import HttpResponse
from .forms import AddForm
from .forms import AddForm_def
from .testfile import testfile

from .func.pir_csv_modify import pir_csv_modify

# Create your views here.

def add(request):
    a = request.GET.get('a', 0)
    b = request.GET.get('b', 0)
    c = int(a) + int(b)
    return HttpResponse(str(c))

def add2(request, a, b):
    c = int(a) + int(b)
    return HttpResponse(str(c))

def index(request):
    return render(request, "index.html")

def plus(request):
    a = request.GET.get('a', None)
    b = request.GET.get('b', None)
    a = int(a)
    b = int(b)
    return HttpResponse(str(a+b))


def index2(request):
    if request.method == 'POST':
        form = AddForm(request.POST)
        if form.is_valid():
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            return HttpResponse(str(int(a) + int(b)))

    else:
        form = AddForm()

    return render(request, "index.html", {'form': form})


def change_csv(request):
    if request.method == 'POST':
        form = AddForm_def(request.POST)
        if form.is_valid():
            def_bw = form.cleaned_data['def_bw']
            pir_csv_modify(def_bw = def_bw)
            #testfile()

            return HttpResponse("successful!")

    else:
        form = AddForm_def()

    return render(request, "change_csv.html", {'form': form})




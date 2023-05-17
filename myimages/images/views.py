from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Image
from .forms import ImageUploadForm


# Create your views here.
def index(request):
    data = Image.objects.all()
    return render(request, "display.html", {'data': data})


def index1(request):
    data1 = Image.objects.all()
    if 'title' in request.session:
        title = request.session['title']
        return render(request, "display1.html", {'data1': data1, 'title': title})
    else:
        return HttpResponse("Your link expired. Please a contact with administrator.")


def index2(request):
    data2 = Image.objects.all()
    context = {
        'data2': data2
    }
    return render(request, "display2.html", context)


def upload_image(request):
    request.session['title'] = 'title'
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index1')
    else:
        form = ImageUploadForm()
    return render(request, 'upload_image.html', {'form': form})



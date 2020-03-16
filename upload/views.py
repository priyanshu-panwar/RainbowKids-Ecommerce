from django.shortcuts import render,redirect
from .models import Upload
# Create your views here.

def upload(request):
    if request.method=='POST':
        name = request.POST.get('name')
        filename = request.POST.get('filename')
        obj = Upload.objects.get_or_create(name=name,image=filename)

        return redirect('shop:product_list')
    return render(request,"upload/upload.html")

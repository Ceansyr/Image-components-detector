from django.shortcuts import render
from django.http import HttpResponse
from MyApi.models import MyFile

from django.conf import settings


def Home(request):
    print("User Request method is", request.method)
    if request.method == "POST":
        img = request.FILES["image"]
        MyFile.objects.create(image = img)


    return render(request, "index.html")


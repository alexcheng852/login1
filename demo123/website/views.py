from django.shortcuts import  render

def index(request):
    return render(request, "website/index.html")

def services(request):
    return render(request, "website/services.html")


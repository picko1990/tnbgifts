from django.shortcuts import render
from .models import Image
from .utils.images import get_owned_images


def index(request):
    images = Image.objects.all()
    context = {"images": images}
    return render(request, "main/index.html", context)


def collection(request):
    address = request.GET.get("address")

    if not address:
        return render(request, "main/collection.html")

    else:
        images = get_owned_images(address=address)
        context = {
            "address": address,
            "images": images
        }
        return render(request, "main/collection.html", context)

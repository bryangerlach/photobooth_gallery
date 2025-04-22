import os
from django.shortcuts import render
from django.conf import settings

def image_gallery(request):
    local_image_path = settings.LOCAL_IMAGE_DIRECTORY
    image_urls = []

    if os.path.isdir(local_image_path):
        for filename in os.listdir(local_image_path):
            if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):
                image_url = f"{settings.STATIC_URL}{filename}"
                image_urls.append(image_url)
    else:
        print(f"Error: Local image directory not found: {local_image_path}")

    return render(request, 'image_gallery.html', {'image_urls': image_urls})
"""
URL configuration for bookstore project.
"""

import debug_toolbar
from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework.authtoken.views import obtain_auth_token
from django.http import JsonResponse, HttpResponse
import os
import subprocess

def home(request):
    return JsonResponse({
        "message": "🚀 Welcome to the Bookstore API!",
        "status": "running",
        "documentation": "https://github.com/Bruno-Alvez/bookstore"
    })

def update_server(request):
    if request.method == "POST":
        project_path = "/home/brunoalvesdev/bookstore"
        os.chdir(project_path)
        result = subprocess.run(["git", "pull"], capture_output=True, text=True)

        wsgi_path = "/var/www/brunoalvesdev_pythonanywhere_com_wsgi.py"
        os.utime(wsgi_path, None)

        return HttpResponse(f"Updated:\n{result.stdout}")
    else:
        return HttpResponse("Only POST requests are allowed.", status=405)

urlpatterns = [
    path('', home),
    path('__debug__/', include(debug_toolbar.urls)),
    path("admin/", admin.site.urls),
    re_path("bookstore/(?P<version>(v1|v2))/", include("order.urls")),
    re_path("bookstore/(?P<version>(v1|v2))/", include("product.urls")),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('update_server/', update_server),
]

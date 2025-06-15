# bookstore/bookstore/views.py
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import git
import os

def home(request):
    return JsonResponse({
        "message": "🚀 Welcome to the Bookstore API!",
        "status": "running",
        "documentation": "https://github.com/Bruno-Alvez/bookstore"
    })

@csrf_exempt
def update_server(request):
    if request.method == "POST":
        try:
            repo = git.Repo('/home/brunoalvesdev/bookstore')
            origin = repo.remotes.origin
            origin.pull()
            os.utime('/var/www/brunoalvesdev_pythonanywhere_com_wsgi.py', None)
            return HttpResponse("✅ Code updated from GitHub.")
        except Exception as e:
            return HttpResponse(f"❌ Update failed: {str(e)}", status=500)
    return HttpResponse("Only POST allowed", status=405)

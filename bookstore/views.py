from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import git
import os
import subprocess

STATIC_DIR = '/home/brunoalvesdev/bookstore/staticfiles'

def home(request):
    return JsonResponse({
        "message": "🚀 Welcome to the Bookstore API!",
        "status": "running",
        "documentation": "https://github.com/Bruno-Alvez/bookstore",
        "endpoints": {
            "products": "/bookstore/v1/product/",
            "categories": "/bookstore/v1/category/",
            "orders": "/bookstore/v1/order/",
            "token_auth": "/api-token-auth/",
            "admin": "/admin/",
        }
    })

@csrf_exempt
def update_server(request):
    if request.method == "POST":
        try:
            repo = git.Repo('/home/brunoalvesdev/bookstore')
            origin = repo.remotes.origin
            origin.pull()

            admin_css_path = os.path.join(STATIC_DIR, 'admin', 'css')
            if not os.path.exists(admin_css_path):
                subprocess.run(
                    ["python3", "manage.py", "collectstatic", "--noinput"],
                    cwd="/home/brunoalvesdev/bookstore"
                )

            os.utime('/var/www/brunoalvesdev_pythonanywhere_com_wsgi.py', None)

            return HttpResponse("✅ Code updated and static assets verified.")
        except Exception as e:
            return HttpResponse(f"❌ Update failed: {str(e)}", status=500)

    return HttpResponse("Only POST allowed", status=405)

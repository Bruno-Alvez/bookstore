from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import git
import os


@csrf_exempt
def update_server(request):
    """
    View para automatizar o deploy via GitHub webhook (POST).
    Realiza git pull no repositório e atualiza o WSGI para refletir mudanças.
    """
    if request.method == "POST":
        try:
            repo = git.Repo('/home/brunoalvesdev/bookstore')
            origin = repo.remotes.origin
            origin.pull()

            os.utime('/var/www/brunoalvesdev_pythonanywhere_com_wsgi.py', None)

            return HttpResponse("✅ Código atualizado com sucesso via GitHub.")
        except Exception as e:
            return HttpResponse(f"❌ Falha ao atualizar o código: {str(e)}", status=500)
    return HttpResponse("Apenas requisições POST são permitidas.", status=405)


def home(request):
    """
    View principal da API. Responde na raiz (/) com uma mensagem de status.
    """
    return HttpResponse("📚 Bookstore API is running! Explore os endpoints disponíveis.")
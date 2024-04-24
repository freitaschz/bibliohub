from django.http import HttpResponse
from django.shortcuts import redirect, render

from acervo.models import AcervoLivrosUsuarios, Livros


# Create your views here.
def pagina_meu_acervo(request):
    id_usuario_logado = request.user.id
    acervo_livros_usuario = AcervoLivrosUsuarios.objects.filter(
        usuario_id=id_usuario_logado
    ).select_related("livro")

    livros = []
    for registro in acervo_livros_usuario:
        livros.append(
            {
                "id_relacao": registro.id,
                "dados_livro": registro.livro,
                "livro_favorito_usuario": registro.livro_favorito,
                "livro_lido_usuario": registro.livro_lido,
            }
        )

    return render(request, "meu_acervo.html", {"acervo_livros": livros})


def pagina_adicionar_no_acervo(request):
    id_usuario_logado = request.user.id
    livros_disponiveis_usuario = Livros.objects.exclude(
        id__in=AcervoLivrosUsuarios.objects.filter(
            usuario_id=id_usuario_logado
        ).values_list("livro", flat=True),
    )
    return render(
        request,
        "adicionar_no_acervo.html",
        {"livros_disponiveis": livros_disponiveis_usuario},
    )


def adicionar_livro_no_acervo_usuario(request):
    if request.method == "POST":
        try:
            id_usuario_logado = request.user.id
            livros_disponiveis_usuario = Livros.objects.exclude(
                id__in=AcervoLivrosUsuarios.objects.filter(
                    usuario_id=id_usuario_logado
                ).values_list("livro__id", flat=True),
            ).values_list("id", flat=True)

            id_livro = int(request.POST.get("livro"))
            livro_favorito = request.POST.get("livroFavorito") == "on"
            livro_lido = request.POST.get("livroLido") == "on"

            if id_livro in livros_disponiveis_usuario:
                livro = Livros.objects.get(id=id_livro)
                AcervoLivrosUsuarios.objects.create(
                    usuario=request.user,
                    livro=livro,
                    livro_favorito=livro_favorito,
                    livro_lido=livro_lido,
                )
        except Exception as e:
            print(f"Um erro inesperado aconteceu! {e}")
        finally:
            return redirect("/meu-acervo")
    return HttpResponse("Método de requisição não permitido!", status=405)


def excluir_livro_do_acervo_usuario(request):
    if request.method == "POST":
        try:
            id_relacao = int(request.POST.get("idRelacao"))
            livro = AcervoLivrosUsuarios.objects.get(id=id_relacao)
            livro.delete()
        except Exception as e:
            print(f"Um erro inesperado aconteceu! {e}")
        finally:
            return redirect("/meu-acervo")
    return HttpResponse("Método de requisição não permitido!", status=405)

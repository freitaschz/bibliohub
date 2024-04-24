"""
URL configuration for bibliohub project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import RedirectView

from acervo.views import (
    adicionar_livro_no_acervo_usuario,
    excluir_livro_do_acervo_usuario,
    pagina_adicionar_no_acervo,
    pagina_meu_acervo,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("meu-acervo/", login_required(pagina_meu_acervo)),
    path("adicionar-livro-acervo/", login_required(pagina_adicionar_no_acervo)),
    path(
        "adicionar-livro-acervo/cadastrar/",
        login_required(adicionar_livro_no_acervo_usuario),
    ),
    path("excluir-livro-acervo/", login_required(excluir_livro_do_acervo_usuario)),
    path("", RedirectView.as_view(url="meu-acervo/", permanent=True)),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

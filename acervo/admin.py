from django.contrib import admin

from acervo.models import AcervoLivrosUsuarios, Autores, Editoras, Generos, Livros


# Register your models here.
class AutoresAdmin(admin.ModelAdmin):
    list_display = [
        "nome_autor",
        "data_nascimento",
        "data_falecimento",
        "data_hora_insercao",
        "data_hora_atualizacao",
    ]
    list_filter = ["data_hora_insercao", "data_hora_atualizacao"]
    search_fields = [
        "nome_autor",
    ]


class EditorasAdmin(admin.ModelAdmin):
    list_display = [
        "nome_editora",
        "cnpj",
        "data_hora_insercao",
        "data_hora_atualizacao",
    ]
    list_filter = ["data_hora_insercao", "data_hora_atualizacao"]
    search_fields = [
        "nome_editora",
        "cnpj",
    ]


class GenerosAdmin(admin.ModelAdmin):
    list_display = [
        "nome_genero",
        "data_hora_insercao",
        "data_hora_atualizacao",
    ]
    list_filter = ["data_hora_insercao", "data_hora_atualizacao"]
    search_fields = [
        "nome_genero",
    ]


class LivrosAdmin(admin.ModelAdmin):
    list_display = [
        "titulo",
        "autor",
        "editora",
        "capa",
        "isbn",
        "obter_generos",
        "data_publicacao",
        "data_hora_insercao",
        "data_hora_atualizacao",
    ]
    list_filter = ["data_publicacao", "data_hora_insercao", "data_hora_atualizacao"]
    search_fields = [
        "titulo",
        "autor__nome_autor",
        "editora__nome_editora",
        "isbn",
    ]

    def obter_generos(self, obj):
        return ", ".join([g.nome_genero for g in obj.genero.all()])


class AcervoLivrosUsuariosAdmin(admin.ModelAdmin):
    list_display = [
        "usuario",
        "livro",
        "livro_favorito",
        "livro_lido",
        "data_hora_insercao",
        "data_hora_atualizacao",
    ]
    list_filter = ["livro__titulo", "data_hora_insercao", "data_hora_atualizacao"]
    search_fields = [
        "usuario__username",
        "usuario__email",
        "usuario__first_name",
        "usuario__last_name",
        "livro__titulo",
    ]


admin.site.register(Autores, AutoresAdmin)
admin.site.register(Editoras, EditorasAdmin)
admin.site.register(Generos, GenerosAdmin)
admin.site.register(Livros, LivrosAdmin)
admin.site.register(AcervoLivrosUsuarios, AcervoLivrosUsuariosAdmin)

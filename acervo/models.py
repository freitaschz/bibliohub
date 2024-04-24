from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Autores(models.Model):
    nome_autor = models.CharField(max_length=255)
    data_nascimento = models.DateField(null=True, blank=True)
    data_falecimento = models.DateField(null=True, blank=True)
    biografia = models.TextField(null=True, blank=True)
    data_hora_insercao = models.DateTimeField(auto_now_add=True)
    data_hora_atualizacao = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autores"

    def __str__(self):
        return self.nome_autor


class Editoras(models.Model):
    nome_editora = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=14, unique=True, null=True, blank=True)
    data_hora_insercao = models.DateTimeField(auto_now_add=True)
    data_hora_atualizacao = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Editora"
        verbose_name_plural = "Editoras"

    def __str__(self):
        return self.nome_editora


class Generos(models.Model):
    nome_genero = models.CharField(max_length=100)
    data_hora_insercao = models.DateTimeField(auto_now_add=True)
    data_hora_atualizacao = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Genero"
        verbose_name_plural = "Generos"

    def __str__(self):
        return self.nome_genero


class Livros(models.Model):
    titulo = models.CharField(max_length=255)
    autor = models.ForeignKey(Autores, on_delete=models.SET_NULL, null=True)
    editora = models.ForeignKey(Editoras, on_delete=models.SET_NULL, null=True)
    capa = models.ImageField(upload_to="livros/capas/%Y/%m/%d", blank=True, default="")
    resumo = models.TextField(null=True, blank=True)
    isbn = models.CharField(max_length=13, unique=True)
    genero = models.ManyToManyField(Generos)
    data_publicacao = models.DateField(null=True, blank=True)
    data_hora_insercao = models.DateTimeField(auto_now_add=True)
    data_hora_atualizacao = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Livro"
        verbose_name_plural = "Livros"

    def __str__(self):
        return self.titulo


class AcervoLivrosUsuarios(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    livro = models.ForeignKey(Livros, on_delete=models.PROTECT)
    livro_lido = models.BooleanField()
    livro_favorito = models.BooleanField()
    data_hora_insercao = models.DateTimeField(auto_now_add=True)
    data_hora_atualizacao = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "AcervoLivrosUsuario"
        verbose_name_plural = "AcervoLivrosUsuarios"

from django.db import models

from portfolio.views import resolution_path_tecnologias
from portfolio.views import resolution_path_posts
from portfolio.views import resolution_path_projects
from portfolio.views import resolution_path_noticias
from portfolio.views import resolution_path_interesses

from portfolio.views import resolution_path_tfc


class Post(models.Model):
    autor = models.CharField(max_length=30)
    titulo = models.CharField(max_length=30)
    descricao = models.CharField(max_length=500)
    data = models.DateField(auto_now_add=True)
    imagem = models.ImageField(upload_to=resolution_path_posts, null=True, blank=True)
    link = models.URLField("Link", max_length=200, null=True, blank=True)

    def __str__(self):
        return self.titulo[:20]


class Projeto(models.Model):
    titulo = models.CharField(max_length=30)
    decricao = models.CharField(max_length=2000)
    ano = models.IntegerField()
    imagem = models.ImageField(upload_to=resolution_path_projects, null=True, blank=True)

    def __str__(self):
        return self.titulo[:20]


class Competencia(models.Model):
    nome = models.CharField(max_length=20)
    decricao = models.CharField(max_length=2000)


class Pessoa(models.Model):
    nome = models.CharField(max_length=30)
    competencias = models.ManyToManyField(Competencia)
    link = models.URLField("Linkedin", max_length=200, null=True, blank=True)

    def __str__(self):
        return self.nome[:20]


class Tecnologia(models.Model):
    nome = models.CharField(max_length=20)
    decricao = models.CharField(max_length=2000)
    acronimo = models.CharField(max_length=20)
    ano = models.IntegerField()
    criador = models.ManyToManyField(Pessoa)
    link = models.URLField("Site Oficial", max_length=200, null=True, blank=True)
    logotipo = models.ImageField(upload_to=resolution_path_tecnologias, null=True, blank=True)


class Cadeira(models.Model):
    nome = models.CharField(max_length=20)
    ano = models.IntegerField()
    semestre = models.CharField(max_length=20)
    descricao = models.CharField(max_length=20)
    ects = models.IntegerField(default="6")
    linguagens = models.ManyToManyField(Tecnologia)
    docente_teorica = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    docentes_praticas = models.ManyToManyField(Pessoa, related_name='caderias')
    projetos = models.ManyToManyField(Projeto)

    def __str__(self):
        return self.nome[:20]


class TFC(models.Model):
    nome = models.CharField(max_length=20)
    ano_realizacao = models.IntegerField()
    resumo = models.TextField()
    autor = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    orientador = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    youtube = models.URLField("Youtube", max_length=200, null=True, blank=True)
    gitHub = models.URLField("GitHub", max_length=200, null=True, blank=True)
    relatorio = models.URLField("Relatório", max_length=200, null=True, blank=True)
    imagem = models.ImageField(upload_to=resolution_path_tfc, null=True, blank=True)


class Interesse(models.Model):
    nome = models.CharField(max_length=20)
    descricao = models.TextField()
    link = models.URLField("link", max_length=200, null=True, blank=True)
    imagem = models.ImageField(upload_to=resolution_path_interesses, null=True, blank=True)


class Noticia(models.Model):
    titulo = models.CharField(max_length=20)
    resumo = models.TextField()
    imagem = models.ImageField(upload_to=resolution_path_noticias)
    link = models.URLField("Link", max_length=200, null=True, blank=True)


class PontuacaoQuizz(models.Model):
    nome = models.CharField(max_length=20)
    pontuacao = models.IntegerField()

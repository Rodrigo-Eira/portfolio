from django.db import models


def resolution_path_posts(instance, filename):
    return f'posts/{instance.id}'


def resolution_path_projects(instance, filename):
    return f'projects/{instance.id}'


def resolution_path_noticias(instance, filename):
    return f'noticias/{instance.id}'


def resolution_path_tecnologias(instance, filename):
    return f'tecnologias/{instance.id}'


def resolution_path_tfc(instance, filename):
    return f'tfc/{instance.id}'


def resolution_path_interesses(instance, filename):
    return f'interesses/{instance.id}'


class Post(models.Model):
    autor = models.CharField(max_length=30)
    titulo = models.CharField(max_length=30)
    descricao = models.CharField(max_length=500)
    data = models.DateField(auto_now_add=True)
    imagem = models.ImageField(upload_to=resolution_path_posts, null=True, blank=True)
    link = models.URLField("Link", max_length=200, null=True, blank=True)

    def __str__(self):
        return self.titulo[:20]


class Competencia(models.Model):
    nome = models.CharField(max_length=20)
    decricao = models.CharField(max_length=2000)

    def __str__(self):
        return self.nome[:20]


class Pessoa(models.Model):
    nome = models.CharField(max_length=30)
    link = models.URLField("Linkedin", max_length=200, null=True, blank=True)

    def __str__(self):
        return self.nome


class Tecnologia(models.Model):
    nome = models.CharField(max_length=20)
    decricao = models.CharField(max_length=2000)
    acronimo = models.CharField(max_length=20)
    ano = models.IntegerField()
    criador = models.ManyToManyField(Pessoa, related_name='criador')
    link = models.URLField("Site Oficial", max_length=200, null=True, blank=True)
    logotipo = models.ImageField(upload_to=resolution_path_tecnologias, null=True, blank=True)


class Interesse(models.Model):
    nome = models.CharField(max_length=20)
    descricao = models.TextField()
    link = models.URLField("link", max_length=200, null=True, blank=True)
    imagem = models.ImageField(upload_to=resolution_path_interesses, null=True, blank=True)


class Noticia(models.Model):
    titulo = models.CharField(max_length=50)
    resumo = models.TextField()
    imagem = models.ImageField(upload_to=resolution_path_noticias, null=True, blank=True)
    link = models.URLField("Link", max_length=200, null=True, blank=True)

    def __str__(self):
        return self.titulo[:50]


class PontuacaoQuizz(models.Model):
    nome = models.CharField(max_length=20)
    pontuacao = models.IntegerField()

    def __str__(self):
        return self.nome[:20]


class TFC(models.Model):
    nome = models.CharField(max_length=50)
    ano_realizacao = models.IntegerField()
    resumo = models.TextField()
    autores = models.ManyToManyField(Pessoa, blank=True, related_name='autores')
    orientador = models.ForeignKey(Pessoa, on_delete=models.CASCADE, related_name='orientador', null=True)
    youtube = models.URLField("Youtube", max_length=200, null=True, blank=True)
    gitHub = models.URLField("GitHub", max_length=200, null=True, blank=True)
    relatorio = models.URLField("Relatório", max_length=200, null=True, blank=True)
    imagem = models.ImageField(upload_to=resolution_path_tfc, null=True, blank=True)

    def __str__(self):
        return self.nome[:50]


class Projeto(models.Model):
    titulo = models.CharField(max_length=30)
    ano = models.IntegerField()
    descricao = models.CharField(max_length=500)
    participantes = models.ForeignKey(Pessoa, on_delete=models.CASCADE, related_name='participantes', null=True,
                                      blank=True)
    imagem = models.ImageField(upload_to=resolution_path_projects, null=True, blank=True)

    def __str__(self):
        return self.titulo[:20]


class Cadeira(models.Model):
    nome = models.CharField(max_length=50)
    ano = models.IntegerField()
    ano_letivo = models.IntegerField()
    semestre = models.CharField(max_length=20)
    descricao = models.CharField(max_length=500)
    ects = models.IntegerField(default="6")
    ranking = models.IntegerField(default="5")
    projetos = models.ManyToManyField(Projeto, blank=True, related_name='projetos')
    docente_teorica = models.ForeignKey(Pessoa, on_delete=models.CASCADE, related_name='docente_teorica')
    docentes_pratica = models.ForeignKey(Pessoa, related_name='docente_pratica', on_delete=models.CASCADE)
    link = models.URLField("Link", max_length=200, null=True, blank=True)

    def __str__(self):
        return self.nome[:50]


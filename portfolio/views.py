from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from matplotlib import pyplot as plt

from .models import Cadeira
from .models import Post
from .models import Projeto
from .models import Competencia
from .models import Tecnologia
from .models import Noticia
from .models import Pessoa
from .models import PontuacaoQuizz
from .models import TFC

from .forms import PostForm
from .forms import CadeiraForm
from .forms import ProjetoForm
from .forms import NoticiaForm
from .forms import TecnologiaForm


def home_page_view(request):
    return render(request, 'portfolio/home.html')


def aboutme_page_view(request):
    elementos = Cadeira.objects.all()

    context = {'cadeiras_1ano_1semestre': elementos.filter(semestre='1ºsemestre', ano=1),
               'cadeiras_1ano_2semestre': elementos.filter(semestre='2ºsemestre', ano=1),
               'cadeiras_2ano_1semestre': elementos.filter(semestre='1ºsemestre', ano=2),
               'cadeiras_2ano_2semestre': elementos.filter(semestre='2ºsemestre', ano=2),
               'cadeiras_3ano_1semestre': elementos.filter(semestre='1ºsemestre', ano=3),
               'cadeiras_3ano_2semestre': elementos.filter(semestre='2ºsemestre', ano=3),
               'competencias': Competencia.objects.all()}

    return render(request, 'portfolio/aboutme.html', context)


@login_required
def aboutme_nova_cadeira_view(request):
    form = CadeiraForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:aboutme'))

    context = {'form': form}

    return render(request, 'portfolio/aboutme_nova_cadeira.html', context)


@login_required
def aboutme_edita_cadeira_view(request, cadeira_id):
    cadeira = Cadeira.objects.get(pk=cadeira_id)
    form = CadeiraForm(request.POST or None, instance=cadeira)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:aboutme'))

    context = {'form': form, 'cadeira_id': cadeira_id}

    return render(request, 'portfolio/aboutme_edita_cadeira.html', context)


@login_required
def aboutme_apaga_cadeira_view(request, cadeira_id):
    Cadeira.objects.get(pk=cadeira_id).delete()
    return HttpResponseRedirect(reverse('portfolio:aboutme'))


def blog_page_view(request):
    context = {'posts': Post.objects.all()}
    return render(request, 'portfolio/blog.html', context)


def blog_novo_post_view(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('portfolio:blog'))
        return render(request, 'portfolio/blog_novo_post.html', {'form': form, 'message': 'Credenciais invalidas.'})

    context = {'form': PostForm()}

    return render(request, 'portfolio/blog_novo_post.html', context)


def blog_edita_post_view(request, post_id):
    post = Post.objects.get(pk=post_id)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('portfolio:blog'))

    context = {'form': PostForm(instance=post), 'post_id': post_id}

    return render(request, 'portfolio/blog_edita_post.html', context)


def blog_apaga_post_view(request, post_id):
    Post.objects.get(pk=post_id).delete()
    return HttpResponseRedirect(reverse('portfolio:blog'))


def contacto_page_view(request):
    return render(request, 'portfolio/contacto.html')


def projetos_page_view(request):
    context = {'projetos': Projeto.objects.all(),
               'tfcs': TFC.objects.all()}
    return render(request, 'portfolio/projetos.html', context)


@login_required
def projetos_novo_projeto_view(request):
    if request.method == "POST":
        form = ProjetoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('portfolio:projetos'))

    context = {'form': ProjetoForm()}

    return render(request, 'portfolio/projetos_novo_projeto.html', context)


@login_required
def projetos_edita_projeto_view(request, projeto_id):
    projeto = Projeto.objects.get(pk=projeto_id)
    if request.method == "POST":
        form = ProjetoForm(request.POST, request.FILES, instance=projeto)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('portfolio:projetos'))

    context = {'form': ProjetoForm(instance=projeto), 'projeto_id': projeto_id}

    return render(request, 'portfolio/projetos_edita_projeto.html', context)


@login_required
def projetos_apaga_projeto_view(request, projeto_id):
    Projeto.objects.get(pk=projeto_id).delete()
    return HttpResponseRedirect(reverse('portfolio:projetos'))


def quizz_page_view(request):
    if request.method == 'POST' and request.POST['nome'] != '':
        n = request.POST['nome']
        p = 0

        if request.POST['opcao'] == 'CSS':
            p = p + 1
        if request.POST['opcao1'] == '2005':
            p = p + 1
        if request.POST['opcao2'] == 'info':
            p = p + 1
        if request.POST['opcao3'] == 'Suíça':
            p = p + 1
        r = PontuacaoQuizz(nome=n, pontuacao=p)
        r.save()

    languages_x = []
    popularity_y = []
    for pontuacao in PontuacaoQuizz.objects.all():
        languages_x.append(pontuacao.nome)
        popularity_y.append(pontuacao.pontuacao)

    languages_x.reverse()
    popularity_y.reverse()
    plt.barh(languages_x, popularity_y)
    plt.savefig('portfolio\static\portfolio\images\plot.png', bbox_inches='tight')
    plt.close()

    return render(request, 'portfolio/quizz.html')


def quiz_apaga(request):
    PontuacaoQuizz.objects.all().delete()
    return HttpResponseRedirect(reverse('portfolio:quizz'))


def site_page_view(request):
    return render(request, 'portfolio/site.html')


def web_page_view(request):
    elementos = Tecnologia.objects.all()

    for elemento in elementos:
        elemento.__dict__["criador"] = list(Pessoa.objects.filter(criador__id=elemento.id))

    context = {'tecnologias': elementos,
               'noticias': Noticia.objects.all()}
    return render(request, 'portfolio/web.html', context)


@login_required
def web_nova_noticia_view(request):
    if request.method == "POST":
        form = NoticiaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('portfolio:web'))

    context = {'form': NoticiaForm()}

    return render(request, 'portfolio/web_nova_noticia.html', context)


@login_required
def web_edita_noticia_view(request, noticia_id):
    noticia = Noticia.objects.get(pk=noticia_id)
    if request.method == "POST":
        form = NoticiaForm(request.POST, request.FILES, instance=noticia)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('portfolio:web'))

    context = {'form': NoticiaForm(instance=noticia), 'noticia_id': noticia_id}

    return render(request, 'portfolio/web_edita_noticia.html', context)


@login_required
def web_apaga_noticia_view(request, noticia_id):
    Noticia.objects.get(pk=noticia_id).delete()
    return HttpResponseRedirect(reverse('portfolio:web'))


@login_required
def web_nova_tecnologia_view(request):
    form = TecnologiaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:web'))

    context = {'form': form}

    return render(request, 'portfolio/web_nova_tecnologia.html', context)


@login_required
def web_edita_tecnologia_view(request, tecnologia_id):
    tecnologia = Tecnologia.objects.get(pk=tecnologia_id)
    form = TecnologiaForm(request.POST or None, instance=tecnologia)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:web'))

    context = {'form': form, 'tecnologia_id': tecnologia_id}

    return render(request, 'portfolio/web_edita_tecnologia.html', context)


@login_required
def web_apaga_tecnologia_view(request, tecnologia_id):
    Tecnologia.objects.get(pk=tecnologia_id).delete()
    return HttpResponseRedirect(reverse('portfolio:web'))


def view_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            request,
            username=username,
            password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('portfolio:home'))
        else:
            return render(request, 'portfolio/login.html', {
                'message': 'Credenciais invalidas.'
            })

    return render(request, 'portfolio/login.html')


def view_logout(request):
    logout(request)

    return render(request, 'portfolio/home.html', {
        'message': 'Foi desconetado.'
    })

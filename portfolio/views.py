from django.shortcuts import render


# Create your views here.

def home_page_view(request):
    return render(request, 'portfolio/home.html')


def aboutme_page_view(request):
    return render(request, 'portfolio/aboutme.html')


def blog_page_view(request):
    return render(request, 'portfolio/blog.html')


def contacto_page_view(request):
    return render(request, 'portfolio/contacto.html')


def projetos_page_view(request):
    return render(request, 'portfolio/projetos.html')


def quizz_page_view(request):
    return render(request, 'portfolio/quizz.html')


def site_page_view(request):
    return render(request, 'portfolio/site.html')


def web_page_view(request):
    return render(request, 'portfolio/web.html')


def resolution_path_posts(instance, filename):
    return f'posts/{instance.id}/'


def resolution_path_projects(instance, filename):
    return f'projects/{instance.id}/'


def resolution_path_noticias(instance, filename):
    return f'noticias/{instance.id}/'


def resolution_path_tecnologias(instance, filename):
    return f'tecnologias/{instance.id}/'


def resolution_path_tfc(instance, filename):
    return f'tfc/{instance.id}/'


def resolution_path_interesses(instance, filename):
    return f'interesses/{instance.id}/'

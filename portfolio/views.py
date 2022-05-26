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

from django.urls import path
from django.shortcuts import render
from . import views

app_name = "portfolio"

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('aboutme', views.aboutme_page_view, name='aboutme'),
    path('aboutme_nova_cadeira', views.aboutme_nova_cadeira_view, name='aboutme_nova_cadeira'),
    path('aboutme_edita_cadeira/<int:cadeira_id>', views.aboutme_edita_cadeira_view, name='aboutme_edita_cadeira'),
    path('aboutme_apaga_cadeira/<int:cadeira_id>', views.aboutme_apaga_cadeira_view, name='aboutme_apaga_cadeira'),
    path('blog', views.blog_page_view, name='blog'),
    path('blog_novo_post', views.blog_novo_post_view, name='blog_novo_post'),
    path('blog_edita_post/<int:post_id>', views.blog_edita_post_view, name='blog_edita_post'),
    path('blog_apaga_post/<int:post_id>', views.blog_apaga_post_view, name='blog_apaga_post'),
    path('contacto', views.contacto_page_view, name='contacto'),
    path('projetos', views.projetos_page_view, name='projetos'),
    path('projetos_novo_projeto', views.projetos_novo_projeto_view, name='projetos_novo_projeto'),
    path('projetos_edita_projeto/<int:projeto_id>', views.projetos_edita_projeto_view, name='projetos_edita_projeto'),
    path('projetos_apaga_projeto/<int:projeto_id>', views.projetos_apaga_projeto_view, name='projetos_apaga_projeto'),
    path('quizz', views.quizz_page_view, name='quizz'),
    path('quizz_apaga', views.quiz_apaga, name='quizz_apaga'),
    path('site', views.site_page_view, name='site'),
    path('web', views.web_page_view, name='web'),
    path('web_novo_noticia', views.web_nova_noticia_view, name='web_nova_noticia_view'),
    path('web_edita_noticia/<int:noticia_id>', views.web_edita_noticia_view, name='web_edita_noticia_view'),
    path('web_apaga_noticia/<int:noticia_id>', views.web_apaga_noticia_view, name='web_apaga_noticia_view'),
    path('web_novo_tecnologia', views.web_nova_tecnologia_view, name='web_nova_tecnologia_view'),
    path('web_edita_tecnologia/<int:tecnologia_id>', views.web_edita_tecnologia_view, name='web_edita_tecnologia_view'),
    path('web_apaga_tecnologia/<int:tecnologia_id>', views.web_apaga_tecnologia_view, name='web_apaga_tecnologia_view'),
    path('login/', views.view_login, name='login'),
    path('logout/', views.view_logout, name='logout'),
]


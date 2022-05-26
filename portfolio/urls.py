from django.urls import path
from django.shortcuts import render
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "portfolio"

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('aboutme', views.aboutme_page_view, name='aboutme'),
    path('blog', views.blog_page_view, name='blog'),
    path('contacto', views.contacto_page_view, name='contacto'),
    path('projetos', views.projetos_page_view, name='projetos'),
    path('quizz', views.quizz_page_view, name='quizz'),
    path('site', views.site_page_view, name='site'),
    path('web', views.web_page_view, name='web')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.forms import ModelForm
from django import forms
from .models import Post
from .models import Projeto
from .models import Cadeira
from .models import Noticia
from .models import Tecnologia



class PostForm(ModelForm):
    descricao = forms.CharField(widget=forms.Textarea(attrs={"rows": 4}))

    class Meta:
        model = Post
        fields = '__all__'


class ProjetoForm(ModelForm):
    descricao = forms.CharField(widget=forms.Textarea(attrs={"rows": 4}))

    class Meta:
        model = Projeto
        fields = '__all__'


class CadeiraForm(ModelForm):
    descricao = forms.CharField(widget=forms.Textarea(attrs={"rows": 3}))

    class Meta:
        model = Cadeira
        fields = '__all__'


class NoticiaForm(ModelForm):
    resumo = forms.CharField(widget=forms.Textarea(attrs={"rows": 3}))

    class Meta:
        model = Noticia
        fields = '__all__'


class TecnologiaForm(ModelForm):
    decricao = forms.CharField(widget=forms.Textarea(attrs={"rows": 3}))

    class Meta:
        model = Tecnologia
        fields = '__all__'


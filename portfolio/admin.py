from django.contrib import admin

from .models import Tecnologia
from .models import Pessoa
from .models import Post
from .models import Projeto
from .models import PontuacaoQuizz
from .models import Competencia
from .models import Noticia
from .models import Interesse
from .models import TFC
from .models import Cadeira

admin.site.register(Cadeira)
admin.site.register(Noticia)
admin.site.register(Post)
admin.site.register(Pessoa)
admin.site.register(PontuacaoQuizz)
admin.site.register(Competencia)
admin.site.register(Interesse)
admin.site.register(TFC)
admin.site.register(Tecnologia)
admin.site.register(Projeto)

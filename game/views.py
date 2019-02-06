from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy

from .models import Jogo, Capitulo_jogo

# Create your views here.
class IndexView(generic.TemplateView):
    template_name = 'game/index.html'


class JogoListView(generic.ListView):
    model = Jogo
    template_name = 'game/jogo_listview.html'

class JogoCreateView(generic.CreateView):
    model = Jogo
    fields = ('nome','descricao')
    template_name = 'game/jogo_novo.html'


class JogoUpdate(generic.UpdateView):
    model = Jogo
    fields = ('nome', 'descricao')
    template_name = 'game/jogo_novo.html'


class JogoDelete(generic.DeleteView):
    model = Jogo
    success_url = reverse_lazy('JogoListView')








class CapituloJogoListView(generic.ListView):
    model = Capitulo_jogo
    template_name = 'game/capitulo_listview.html'

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        capitulo = Capitulo_jogo.objects.filter(chave_estrangeira=pk)
        return capitulo
    

class CapituloJogoDetailView(generic.DetailView):
    model = Capitulo_jogo
    template_name = 'game/capitulo_detail.html'
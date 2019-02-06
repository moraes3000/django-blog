from django.urls import path

from . import views
# app_name para colocar auxiliar a chmar a url ex:polls:detail
# chmar url {% url 'polls:detail' question.id %}

# caso nao tenha colocar o nome no proprio name ex:name='polls_detail'
# chmar url {% url 'polls_detail' question.id %}


urlpatterns = [
    
    #home para  noticia
    path('', views.IndexView.as_view(), name='IndexView'),
  
    #lista os jogos
    path('lista/', views.JogoListView.as_view(), name='JogoListView'),
    path('novo/',views.JogoCreateView.as_view(), name='novo-jogo'),
    path('update/<int:pk>', views.JogoUpdate.as_view(), name='update-jogo'),
    path('delete/<int:pk>', views.JogoDelete.as_view(), name='delete-jogo'),

#
    path('lista/<int:pk>/', views.CapituloJogoListView.as_view(), name='CapituloJogoListView'),
    path('capitulo/<int:pk>/',views.CapituloJogoDetailView.as_view(), name='CapituloJogoDetailView')

   
    
]
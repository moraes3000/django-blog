from django.urls import path

from . import views
# app_name para colocar auxiliar a chmar a url ex:polls:detail
# chmar url {% url 'polls:detail' question.id %}

# caso nao tenha colocar o nome no proprio name ex:name='polls_detail'
# chmar url {% url 'polls_detail' question.id %}
app_name = 'polls'

urlpatterns = [
    
    # ex: /polls/
    path('', views.IndexView.as_view(), name='index'),
    # ex: /polls/5/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # ex: /polls/5/results/
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
    
]
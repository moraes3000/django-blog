from django.contrib import admin

# Register your models here.
from .models import Question , Choice


admin.site.register(Choice)

class QuestionAdmin(admin.ModelAdmin):
   list_display = ('question_text', 'pub_date', 'was_published_recently')   #lista de item para o django
   list_filter = ['pub_date'] #filtro por data
   search_fields = ['question_text'] #campo de pesquisa


admin.site.register(Question, QuestionAdmin)
from django.urls import reverse

from django.db import models
# from ckeditor_uploader.fields import RichTextUploadingField

from django.utils.translation import gettext_lazy as _
from django.db.models.signals import pre_save
from django.dispatch import receiver
from ckeditor.fields import RichTextField

# Create your models here.

class Jogo(models.Model):
    nome = models.CharField(_("nome"), max_length=150)
    slug = models.SlugField(_("slug"), blank=True)
    descricao = RichTextField(u'Conteúdo', default='', blank=True, null=True)
    # #para o ckeditor

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('JogoListView')

    def generate_slug(self):
        from django.template.defaultfilters import slugify
        return slugify(self.nome)

@receiver(pre_save, sender=Jogo)
def my_handler(sender, instance, **kwargs):
    instance.slug = instance.generate_slug()


class Capitulo_jogo(models.Model):
    nome = models.CharField(_("nome"), max_length=150)
    slug = models.SlugField(_("slug"), blank=True)
    chave_estrangeira = models.ForeignKey("Jogo", verbose_name=_("jogo"), on_delete=models.CASCADE)

    def __str__(self):
        return self.nome    

    def generate_slug(self):
        from django.template.defaultfilters import slugify
        return slugify(self.nome)
    
from django.db import models


class Inscricao(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=300)
    tipo_pessoa = models.CharField(max_length=100)
    cpf_cnpj = models.CharField('cpf_cnpj', max_length=20, unique=True)
    rg = models.CharField(max_length=25, unique=True)
    idade = models.IntegerField()
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=20, blank=True)
    criado_em = models.DateTimeField('criado em', auto_now_add=True)

    class Meta:
        ordering = ['criado_em']
        verbose_name = (u'nome')
        verbose_name_plural = (u'nomes')

    def __unicode__(self):
        return self.nome


    

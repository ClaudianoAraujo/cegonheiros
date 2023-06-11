from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

class Chapa(models.Model):
    
    username = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    cel = models.CharField(max_length=255, null=False, blank=False)
    estado = models.CharField(max_length=255, null=False, blank=False)
    cidade = models.CharField(max_length=255, null=False, blank=False)
    descricao = models.TextField(null=True, blank=True)
    data = models.DateTimeField(auto_now=True,)
    img = models.URLField(default='https://www.dataex.com.br/wp-content/uploads/2021/05/inteligencia-artificial-o-que-e-como-funciona-e-aplicacoes-praticas.jpg')
    def __str__(self):
        return f"{self.username}   {self.cel}"
    

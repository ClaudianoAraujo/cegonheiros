from django.urls import path
from . import views

urlpatterns = [
    #path("detalhe/<int:id>/", views.detalhe, name='detalhe'),
    path("post/<int:id>/", views.post, name='post'),
    
]
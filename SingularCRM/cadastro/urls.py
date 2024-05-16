from django.urls import path
from .views import empresa, base

app_name = 'cadastro'

urlpatterns = [
    # Empresa
    # cadastro/empresa/adicionar/
    path(r'empresa/adicionar/',
        empresa.AdicionarEmpresaView.as_view(), name='addempresaview'),
    # cadastro/empresa/listaempresas
    path(r'empresa/listaempresas/',
        empresa.EmpresasListView.as_view(), name='listaempresasview'),
    # cadastro/empresa/editar/
    path(r'empresa/editar/<int:pk>/',
        empresa.EditarEmpresaView.as_view(), name='editarempresaview'),
]
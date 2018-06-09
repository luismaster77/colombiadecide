from django.conf.urls import url
from colombiaDecide import views, models
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^$', login_required(views.base), name='base'),
    #URLS PARA MANDATOS
    url(r'^mandatos/$', views.MandatosListView.as_view(), name='mandatos-list'),
    url(r'^mandatos/(?P<pk>\d+)/detail/$', views.MandatosDetailView.as_view(), name='mandato-detail'),
    url(r'^mandatos/(?P<pk>\d+)/update/$', views.MandatosUpdate.as_view(),name='mandatos-update'),
    #Create mandato
    url(r'^mandatos/create/$', views.MandatosCreate.as_view(), name='mandatos-create'),
    #Delete mandato
    url(r'^mandatos/(?P<pk>\d+)/delete/$', views.MandatosDelete.as_view(), name='mandatos-delete'),
    #URLS PARA USUARIOS
    url(r'^usuarios/create/$', views.UsuariosCompleteCreate.as_view(), name='usuarios_complete-create'),
    url(r'^usuarios/$', views.UsuariosListView.as_view(), name='usuarios-list'),
    url(r'^usuarios/(?P<pk>\d+)/detail/$', views.UsuariosDetailView.as_view(), name='usuario-detail'),
    url(r'^usuarios/(?P<pk>\d+)/update/$', views.UsuariosUpdate.as_view(),name='usuarios-update'),
    #Create mandato
    url(r'^usuarios/create/$', views.UsuariosCreate.as_view(), name='usuarios-create'),
    #Delete mandato
    url(r'^usuarios/(?P<pk>\d+)/delete/$', views.UsuariosDelete.as_view(), name='usuarios-delete'),
]
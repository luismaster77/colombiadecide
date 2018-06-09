# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from colombiaDecide.models import Mandato, Usuarios, VotosConsulta
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator
from django.contrib.auth import login, authenticate, logout
# Create your views here.
@login_required
def base(request):
    return render(request , "base.html")

class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls):
        return login_required(super(LoginRequiredMixin, cls).as_view())

class MandatosListView(LoginRequiredMixin, ListView):
    model = Mandato

class MandatosDetailView(LoginRequiredMixin, DetailView):
    model = Mandato

class MandatosUpdate(UpdateView):
 login_required = True
 model = Mandato
 fields = '__all__'

class MandatosCreate(CreateView):
 login_required = True
 model = Mandato
 fields = '__all__'

class MandatosDelete(DeleteView):
 login_required = True
 model = Mandato
 success_url = reverse_lazy('mandatos-list')

def mandato_list(request):
    mandato_list = Mandato.objects.all()
    context = {'object_list': mandato_list}
    template_name='colombiaDecide/mandato_detail.html'
    return render(request,'colombiaDecide/mandato_list.html', context)

class UsuariosListView(LoginRequiredMixin, ListView):
    model = Usuarios

class UsuariosDetailView(LoginRequiredMixin, DetailView):
    model = Usuarios

class UsuariosUpdate(UpdateView):
 login_required = True
 model = Usuarios
 fields = '__all__'

class UsuariosCreate(CreateView):
 login_required = True
 model = Usuarios
 fields = '__all__'

 @method_decorator(permission_required('usuarios.usuarios-create',reverse_lazy('usuarios:usuarios')))
 def dispatch(self, *args, **kwargs):
    return super(UsuariosCreate, self).dispatch(*args, **kwargs)


class UsuariosCompleteCreate(CreateView):
 login_required = True
 model = Usuarios
 fields = '__all__'
 success_url = reverse_lazy('mandatos-list')

def auth(request):
    if login_required==True:
        if(authenticate.is_active):
            pass
    else:
        success_url = reverse_lazy('mandatos-list')


class UsuariosDelete(DeleteView):
 login_required = True
 model = Usuarios
 success_url = reverse_lazy('usuarios-list')

def usuario_list(request):
    usuario_list = Usuarios.objects.all()
    context = {'object_list': usuario_list}
    template_name='colombiaDecide/usuario_detail.html'
    return render(request,'colombiaDecide/usuario_list.html', context)

def votosConsulta(request):
    votosSi = 0
    if request.POST.get('click', True):
        votosSi = votosSi + 1
        resultado = votosSi
        if resultado > 0:
            p = VotosConsulta(
                id_votos='1',
                id_usuario='3',
                total_si=resultado)
            p.save()

        return render(request,'colombiaDecide/usuarios_list.html')
from gestion.forms import CreateUserForm
from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.views.generic import TemplateView

class Index(TemplateView):
    template_name   = "gestion/index.html"

class CreateUser(SuccessMessageMixin, CreateView):
    template_name   = 'gestion/user_form.html'
    form_class      = CreateUserForm
    success_url     = reverse_lazy('gestion:index')
    success_message = "Votre compte utilisateur a été correctement créé !"
    def get_context_data(self, **kwargs):
        ctx     = super(CreateUser, self).get_context_data(**kwargs)
        ctx['button']    = 'Créer'
        ctx['sec_title'] = "Création d'utilisateur"
        return ctx

from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from django.core.urlresolvers import reverse_lazy
from .views import Index
from .views import CreateUser

from gestion.views import Index

app_name = 'gestion'
urlpatterns = [
        # INDEX
        url(r'^$', Index.as_view(), name="index"),    
        # CREATE USER
        url('^create/$', CreateUser.as_view(), name='create_user'),
        # LOGIN
        url('^login/$',
            auth_views.login,
            {   'template_name': 'gestion/user_login.html',
                'extra_context': {
                    'sec_title' : 'Connexion',
                    'button'    : 'Se connecter',
                    },
            },
            name='login',
        ),
        # LOGOUT
        url('^logout/$', 
            auth_views.logout,
            {   'next_page': reverse_lazy('gestion:index'),
            },
            name='logout',),
        # PASSWORD_CHANGE
        url('^password_change/$',
            auth_views.password_change,
            {   'template_name': 'gestion/user_change_pass.html',
                'post_change_redirect': reverse_lazy('erkan:index'),
                'extra_context': {
                    'sec_title' : 'Changement de mot de passe',
                    'button'    : 'Modifier',
                    },
                },
            name='password_change'),
        # url('^password_change/done/$', name='password_change_done'),
        # RESET PASSWORD
        url('^password_reset/$',
            auth_views.password_reset,
            {   'template_name' : 'gestion/user_password_reset.html',
                'email_template_name': 'gestion/email_password_reset.html',
                'subject_template_name': 'subject_password_reset.txt',
                'post_reset_redirect': reverse_lazy('gestion:password_reset_done'),
                'extra_context': {
                    'sec_title' : 'Demande de nouveau mot de passe',
                    'button'    : 'Envoyer'
                    },
                },
            name='password_reset'),
        # PASS RESET DONE
        url('^password_reset/done/$', 
            Index.as_view(),
            name='password_reset_done'),
        # PASS RESET CONFIRM
        url('^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', 
            auth_views.password_reset_confirm,
            {
                'template_name': 'gestion/user_form.html',
                'post_reset_redirect' : reverse_lazy('gestion:password_reset_complete'),
                'extra_context': {
                    'sec_title' : 'Changer de mot de passe',
                    'button'    : 'Changer'
                    },
                },
            name='password_reset_confirm'),
        # PASS RESET COMPLETE
        url('^reset/done/$',
            Index.as_view(),
            name='password_reset_complete'),
        ]

# Inclu les vues suivantes :

# ^login/$ [name='login']
# ^logout/$ [name='logout']
# ^password_change/$ [name='password_change']
# ^password_change/done/$ [name='password_change_done']
# ^password_reset/$ [name='password_reset']
# ^password_reset/done/$ [name='password_reset_done']
# ^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$ [name='password_reset_confirm']
# ^reset/done/$ [name='password_reset_complete']

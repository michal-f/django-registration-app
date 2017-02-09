from django.conf.urls import url, include
from django.contrib import admin
from register.views import *
from registration.backends.hmac.views import RegistrationView
from register.forms import MyCustomUserForm

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', IndexView.as_view(), name='index'),

    url(r'^accounts/register/$',
        RegistrationView.as_view(
            form_class=MyCustomUserForm
        ),
        name='registration_register',
    ),

    url(r'^accounts/', include('registration.backends.hmac.urls')),  # HMAC REGISTRATION
    url(r'^accounts2/', include('registration.backends.simple.urls')),  # AUTOREGISTRATION
    url(r'^accounts3/', include('registration.backends.model_activation.urls')),  # MODEL BASED

]

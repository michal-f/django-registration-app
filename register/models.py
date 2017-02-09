from __future__ import unicode_literals

from django.contrib import auth
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.signals import user_logged_in
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import PermissionDenied
from django.core.mail import send_mail
from django.db import models
from django.db.models.manager import EmptyManager
from django.utils import six, timezone
from django.utils.deprecation import CallableFalse, CallableTrue
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _


from django.db import models
from django.utils.translation import ugettext_lazy as _

from django.contrib.auth.models import AbstractUser

class MyUser(AbstractUser):
    # extra=models.TextField()

    extra = models.CharField(
        _('extra'),
        max_length=180,
        unique=True,
        help_text=_('Required. XXXX 180 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        error_messages={
            'unique': _("A userXXXXwith that username already exists."),
        },
    )

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _


class Profile(AbstractUser):

    birthdate = models.DateTimeField(_("Birth Date"),
                                     null=True, blank=True)

    picture = models.ImageField(_("Profile Picture"),
                                upload_to="users/avatars/",
                                null=True, blank=True)

    about = models.CharField(_(u"About"), max_length=300, null=True, blank=True)

    def __unicode__(self):
        return u"%s" % self.username




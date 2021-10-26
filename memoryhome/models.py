from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.urls.base import reverse
from datetime import datetime


class Memory(models.Model):
    memory = models.TextField(_("memory body"))
    created = models.DateTimeField(_("created"),auto_now_add=True)
    photo = models.ImageField(_("memory image"), upload_to='images', blank=True, null=True)

    def __str__(self):
        return f"{self.memory[:10]} - {datetime.strftime(self.created, '%d-%m-%y %H:%M:%S')}"

    def get_absolute_url(self):
        return reverse("memoryhome:memory_detail", kwargs={"pk": self.pk})
    
from django.db import models

# Create your models here.
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

# use settings.AUTH_USER_MODEL as foreign key
# pass = todolistpass


class Group(models.Model):
    name = models.CharField(max_length=100, help_text=_('Enter a group name'),  verbose_name=_('name'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('group')
        verbose_name_plural = _('groups')


class TodoList(models.Model):
    title = models.CharField(max_length=250, help_text=_('a title for your to-do item'), verbose_name=_('title'))
    description = models.TextField(blank=True, help_text=_('a description for to-do item'), verbose_name=_('description'))
    created = models.DateField(default=timezone.now, blank=True, verbose_name=_('created'), help_text=_('creation date of to-do item'))
    group = models.ForeignKey(Group, default="general", blank=True, null=True, help_text=_('group of to-do item'), verbose_name=_('group'), on_delete=models.SET_NULL)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, help_text=_('user that the to-do items belongs to'), verbose_name=_('user'), on_delete=models.CASCADE)

    ITEM_STATUS = (
        ('p', _('Pending')),
        ('d', _('Done'))
    )

    status = models.CharField(
        max_length=1,
        choices=ITEM_STATUS,
        blank=True,
        default='p',
        help_text=_('to-do item status'),
        verbose_name=_('status')
    )

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title



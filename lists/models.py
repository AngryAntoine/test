from django.db import models


class Item(models.Model):
    title = models.CharField(max_length=120, null=False, blank=False)
    text = models.TextField()

    def __unicode__(self):
        if not self.title:
            return 'To do item №%d' % self.pk
        return '%s' % self.title

    def __str__(self):
        if not self.title:
            return 'To do item №%d' % self.pk
        return '%s' % self.title

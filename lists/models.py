from django.db import models


class Item(models.Model):
    title = models.CharField(max_length=120, null=False, blank=False)
    text = models.TextField()

    def __unicode__(self):
        return '%s' % self.title


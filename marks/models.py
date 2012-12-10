from django.db import models
from django.contrib.auth.models import User

from marks.managers import MarkManager

# requires django-taggit
from taggit.managers import TaggableManager

# Create your models here.
class Mark(models.Model):
    name = models.CharField(max_length=255, unique=True)
    tag = TaggableManager()
    created_at = models.DateTimeField(auto_now_add=True)

    objects = MarkManager()

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ["-created_at"]
        get_latest_by = "created_at"

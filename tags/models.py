from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

# Create your models here.
class Tag(models.Model):
    label = models.CharField(max_length=50)

class TaggedItem(models.Model):
    # what tag is applied to what object
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    # if we want to tag a product, we can use this field but it will be dependent on store app we dont want that
    # product = models.ForeignKey(Product, on_delete=models.CASCADE)

    # Type (product, video, article, etc.)
    # ID
    content_type = models.ForeignKey(ContentType,on_delete=models.CASCADE)
    # we have this django.contrib.contenttypes in installed apps which we can use for generic relations
    object_id = models.PositiveIntegerField()
    # this is the id of the object we are tagging
    content_object = GenericForeignKey()
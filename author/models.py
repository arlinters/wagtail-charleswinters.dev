from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.models import register_snippet

@register_snippet
class Author(models.Model):
  image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
  first_name = models.CharField(max_length=25)
  last_name = models.CharField(max_length=25)
  github_username = models.CharField(max_length=25)
  github_url = models.CharField(max_length=50)
 
  panels = [
    ImageChooserPanel('image'),
    MultiFieldPanel([
      FieldPanel('first_name'),
      FieldPanel('last_name')
    ], heading='Name'),
    
    MultiFieldPanel([
      FieldPanel('github_username'),
      FieldPanel('github_url')
    ], heading='Github Info')
  ]

  def __str__(self) -> str:
    return self.first_name
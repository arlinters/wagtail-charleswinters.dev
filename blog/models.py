from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core.blocks import StreamBlock, RichTextBlock, CharBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtailmarkdown.blocks import MarkdownBlock
from wagtailmarkdown.fields import MarkdownField
from wagtailmarkdown.edit_handlers import MarkdownPanel
from streams.blocks import CommonContentStreamBlock

class BlogLandingPage(Page):
  def get_context(self, request, *args, **kwargs):
      context =  super().get_context(request, *args, **kwargs)
      context['posts'] = BlogPost.objects.all()
      return context
   
# Create your models here.
class BlogPost(Page):
  body = StreamField([
    	('rich_text', RichTextBlock(icon='pilcrow', template='streams/content/rich_text.html')),
      ('markdown', MarkdownBlock(icon='pilcrow', template='streams/content/markdown.html')),
      ('h1', CharBlock(icon='title', template='streams/content/h1.html')),
      ('h2', CharBlock(icon='title', template='streams/content/h2.html')),
      ('h3', CharBlock(icon='title', template='streams/content/h3.html')),
      ('h4', CharBlock(icon='title', template='streams/content/h4.html')),
      ('h5', CharBlock(icon='title', template='streams/content/h5.html')),
      ('h6', CharBlock(icon='title', template='streams/content/h6.html')),
      ('image', ImageChooserBlock(icon='image', template='streams/content/content/image.html')),
  ])
  preview_text = models.CharField(max_length=150)
  
  author = models.ForeignKey(
        'author.Author',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
	)
  content_panels = Page.content_panels + [
		SnippetChooserPanel("author"),
    FieldPanel("preview_text"),
		StreamFieldPanel("body")
  ]
	

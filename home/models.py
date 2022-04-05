from django.db import models

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from blog.models import BlogPost
class HomePage(Page):
    author = models.ForeignKey(
        'author.Author',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    content_panels = Page.content_panels + [
        SnippetChooserPanel('author'),
    ]
    def get_context(self, request, *args, **kwargs):
        context =  super().get_context(request, *args, **kwargs)
        context['latest_post'] = BlogPost.objects.all().order_by('-first_published_at').first()
        return context
    
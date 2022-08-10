from django.db import models

from wagtail.models import Page, StreamField
from wagtail.blocks import RichTextBlock
from wagtail.admin.edit_handlers import FieldPanel
# Create your models here.

class BlogPage(Page):
    content = StreamField([
       ('rich_text', RichTextBlock(
           template='blocks/rich_text_content.html',
           features=['bold','italic','ol','ul','hr','link','document-link','image','embed']
       )), 
    ], use_json_field=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('content'),
    ]

from wagtail.core.blocks import (
  StreamBlock,
  StructBlock,
  RichTextBlock,
  CharBlock  
)
from wagtail.images.blocks import ImageChooserBlock
from wagtailmarkdown.blocks import MarkdownBlock

class CommonContentStreamBlock(StreamBlock):
	rich_text = RichTextBlock(icon='pilcrow', template='streams/content/rich_text.html')
	markdown = MarkdownBlock(icon='pilcrow', template='streams/content/markdown.html')
	h1 = CharBlock(icon='title', template='streams/content/h1.html')
	h2 = CharBlock(icon='title', template='streams/content/h2.html')
	h3 = CharBlock(icon='title', template='streams/content/h3.html')
	h4 = CharBlock(icon='title', template='streams/content/h4.html')
	h5 = CharBlock(icon='title', template='streams/content/h5.html')
	h6 = CharBlock(icon='title', template='streams/content/h6.html')
	image = ImageChooserBlock(icon='image', template='streams/content/content/image.html')

	class Meta:
		icon='pilcrow'
		template='streams/content/base.html'
  
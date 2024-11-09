from django import template
from ..models import Post
from django.utils.safestring import mark_safe
import markdown
register = template.Library()
@register.simple_tag
def comments_count(post_id):
    return Post.published.get(pk=post_id).comments.count()

@register.filter(name='markdown')
def markdown_format(text):
    return mark_safe(markdown.markdown(text))
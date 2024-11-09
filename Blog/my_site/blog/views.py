from audioop import reverse
from crypt import methods
from ctypes.wintypes import PSIZE

from django.contrib.gis.gdal.prototypes.srs import release_srs
from taggit.models import Tag

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from .forms import CommentForm


def paginator_view(request, post_list):
    paginator = Paginator(post_list, '3')
    page_num = request.GET.get('page', 1)
    try:
        posts = paginator.page(page_num)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        posts = paginator.page(1)
    return posts

def post_list(request):
    post_list_news = Post.published.order_by('-created')[:5]
    post_list = Post.published.all()
    posts = paginator_view(request, post_list)
    return render(request, 'blog/post_list.html', {'posts': posts, 'post_list_news': post_list_news})

def post_list_tags(request, tags_slug=None):
    tag = None
    posts = Post.published.all()
    if tags_slug:
        tag = get_object_or_404(Tag, slug=tags_slug)
        posts = posts.filter(tags__in=[tag])
    posts = paginator_view(request, posts)
    context = {
        'tag': tag,
        'posts': posts,
    }
    return render(request, 'blog/tag_post_list.html', context)



def detail_post(request, year, month, day, post_slug):
    post = get_object_or_404(Post,
                            publish__year = year,
                            publish__month = month,
                            publish__day = day,
                            slug = post_slug,
                            status=Post.Status.PUBLISHED)

    comments_list = post.comments.all()
    post_tags_ids = post.tags.values_list('id', flat=True)
    related_posts = Post.published.filter(tags__in = post_tags_ids).exclude(id=post.id)[:3]
    if request.method == 'POST':
        form_comment = CommentForm(request.POST)
        if form_comment.is_valid():
            comment = form_comment.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('blog:detail_post', year, month, day, post_slug)
    else:
        form_comment = CommentForm()
    return render(request, 'blog/post.html', {'post': post, 'form_comment': form_comment, 'comments': comments_list, 'related_posts': related_posts})

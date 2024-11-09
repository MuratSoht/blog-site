from django.urls import path
from .views import post_list, detail_post, post_list_tags

app_name = 'blog'
urlpatterns = [
    path('', post_list, name='home'),
    path('tag/<slug:tags_slug>/', post_list_tags, name='post_list_tags'),
    path('<int:year>/<int:month>/<int:day>/<slug:post_slug>/', detail_post, name='detail_post'),
]
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


from posts.views import (
    authorSettings,
    post_list_cat, 
    posts_list_user,
    posts_list_author, 
    post_create, 
    post_update, 
    

    IndexView,
    PostListView,
    PostDetailView,
    #PostCreateView,
    #PostUpdateView,
    PostDeleteView,
    SearchView
    )



urlpatterns = [
    path('admin/', admin.site.urls),

    path('', IndexView.as_view(), name='home'),

    #path('blog/', post_list, name='post-list'),
    path('category/<str:cat_name>/', post_list_cat, name='post-cat'),
    path('author/<str:author>/', posts_list_author, name='post-author'),
    path('author/<str:user>/', posts_list_user, name='post-user'),


    path('blog/<str:user_name>/', posts_list_user, name='posts-user'),
    path('blog/', PostListView.as_view(), name='post-list'),

    #path('post/<id>/', post_detail, name='post-detail'),
    path('post/<pk>/', PostDetailView.as_view(), name='post-detail'),


    path('create/', post_create, name='post-create'),
    #path('create/', PostCreateView.as_view(), name='post-create'),

    path('post/<id>/update/', post_update, name='post-update'),             #path('post/<pk>/update', PostUpdateView.as_view(), name='post-update'),

    #path('post/<pk>/delete', post_delete, name='post-delete'),
    path('post/<pk>/delete', PostDeleteView.as_view(), name='post-delete'),

    #path('search/', search, name='search'),
    path('search/', SearchView.as_view(), name='search'),

    path('tinymce/', include('tinymce.urls')),
    
    path('accounts/', include('allauth.urls')),
    #path('accounts/profile/', user_profile, name='user-profile' ),
    path('accounts/profile/', authorSettings, name='author-settings')

    
    
    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

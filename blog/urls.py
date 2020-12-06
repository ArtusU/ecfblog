from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


from posts.views import (
    index, 
    user_profile,
    authorSettings,
    post_list,
    post_list_cat, 
    post_detail, 
    search, 
    post_create, 
    post_update, 
    post_delete,
    

    IndexView,
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    SearchView
    )



urlpatterns = [
    path('admin/', admin.site.urls),

    path('', IndexView.as_view(), name='home'),

    #path('blog/', post_list, name='post-list'),
    path('blog/cat', post_list_cat, name='post-list'),
    path('blog/', PostListView.as_view(), name='post-list'),

    #path('post/<id>/', post_detail, name='post-detail'),
    path('post/<pk>/', PostDetailView.as_view(), name='post-detail'),


    #path('create/', post_create, name='post-create'),
    path('create/', PostCreateView.as_view(), name='post-create'),

    #path('post/<pk>/update', post_update, name='post-update'),
    path('post/<pk>/update', PostUpdateView.as_view(), name='post-update'),

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

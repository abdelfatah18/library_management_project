from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/accounts/', include('accounts.urls')),
    path('api/library/', include('library.urls')),
    path('api/bookshelf/', include('bookshelf.urls')),
    path('api/book/', include('book.urls')),
    path('api/posts/', include('posts.urls')),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    
    
]
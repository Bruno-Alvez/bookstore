# bookstore/bookstore/urls.py
from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework.authtoken.views import obtain_auth_token
from bookstore.views import update_server, home
import debug_toolbar

urlpatterns = [
    path('', home),
    path('__debug__/', include(debug_toolbar.urls)),
    path("admin/", admin.site.urls),
    re_path("bookstore/(?P<version>(v1|v2))/", include("order.urls")),
    re_path("bookstore/(?P<version>(v1|v2))/", include("product.urls")),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('update_server/', update_server),
]

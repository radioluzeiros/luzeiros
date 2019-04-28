"""
luzeiros URL Configuration
https://docs.djangoproject.com/en/2.1/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from rest_framework_swagger.views import get_swagger_view
from rest_framework_simplejwt import views as jwt_views

api_schema_docs = get_swagger_view(title='Luzeiros API')

urlpatterns = [
    # Application urls
    path('', include('luzeiros.core.urls')),
    path('', include('luzeiros.blog.urls')),
    path('', include('luzeiros.radio.urls')),

    # Administrative dashboard
    path('admin/', admin.site.urls),

    # Documentation endpoint
    path('documentation/', api_schema_docs),

    # Application urls
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]

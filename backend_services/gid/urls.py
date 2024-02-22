"""
URL configuration for gid project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi




from .settings import (
    FUNCTION_APP_PATH,
    STATIC_URL,
    DEBUG,
)


admin.site.site_header  =  "GID Super Admin View"  

schema_view = get_schema_view(
    openapi.Info(
        title="GID API",
        default_version='v1',
        description="GID API LIST",
        terms_of_service="",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path(FUNCTION_APP_PATH + '/admin/', admin.site.urls),
    path(FUNCTION_APP_PATH + '/profiles/', include('profiles.urls')),
    path(FUNCTION_APP_PATH + '/products/', include('products.urls')),
    path(FUNCTION_APP_PATH + '/payments/', include('payments.urls')),
    path(FUNCTION_APP_PATH + '/orders/', include('orders.urls')),
    path(FUNCTION_APP_PATH + '/categories/', include('categories.urls')),
    path(FUNCTION_APP_PATH + '/carts/', include('carts.urls')),
    path(FUNCTION_APP_PATH + '/bills/', include('bills.urls')),
    path(FUNCTION_APP_PATH + '/addresses/', include('addresses.urls')),

    path(FUNCTION_APP_PATH + '/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path(FUNCTION_APP_PATH + '/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path(FUNCTION_APP_PATH + '/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]

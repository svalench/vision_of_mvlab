"""project_v_0_0_1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from api.router import router
from structure.router import router1
from recorder.router import router_recorder

# from rest_framework.schemas import get_schema_view

from django.views.generic import TemplateView

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Test api",
        default_version='v0.1',
        description="Test APIs for dashboard"
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

from django.conf.urls import url


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    # path('structure/', include('structure.urls')),
    path('structure/', include(router1.urls)),
    path('settings/',include('structure.urls')),
    path('user/', include('users.urls')),
    path('recorder/', include('recorder.urls')),
    path('recorder/structure/', include(router_recorder.urls)),
    path('dashboard/', include('api.urls')),
    # path('openapi/', get_schema_view(
    #         title="School Service",
    #         description="API developers hpoing to use our service"
    #     ), name='openapi-schema'),
    # path('docs/', TemplateView.as_view(
    #         template_name='documentation.html',
    #         extra_context={'schema_url':'openapi-schema'}
    #     ), name='swagger-ui'),

    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]

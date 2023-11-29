"""
URL configuration for Project project.

The `urlpatterns` list routes URLs to users. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function users
    1. Add an import:  from my_app import users
    2. Add a URL to urlpatterns:  path('', users.home, name='home')
Class-based users
    1. Add an import:  from other_app.users import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from users import urls as users_app_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('', include(users_app_urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

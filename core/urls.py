from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # admin route
    path('admin/', admin.site.urls),
    # user route
    path('api/user/', include('users.urls')),
    # blog route
    path('api/blog/', include('blog.urls')),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
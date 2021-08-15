from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    # api docs
    path('', include_docs_urls(title='Blog API')),
    path('schema/', get_schema_view(
        title="Blog API",
        description="API for the Blog",
        version="1.0.0"
    ), name='openapi-schema'),

    # admin route
    path('admin/', admin.site.urls),
    # user route
    path('api/user/', include('users.urls')),
    # blog route
    path('api/blog/', include('blog.urls')),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
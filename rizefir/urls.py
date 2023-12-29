
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rizefir.views import IndexView, AboutView

urlpatterns = [
    path("admin/", admin.site.urls),
    path('products/', include('rizefir.products.urls')),
    path('users/', include('rizefir.users.urls', namespace='users')),
    path('', IndexView.as_view(), name='index'),
    path('about/', AboutView.as_view(), name='about')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
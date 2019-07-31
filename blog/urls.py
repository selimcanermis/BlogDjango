from django.contrib import admin
from django.urls import path, include
from home.views import home_view
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    #path('', include('post.urls')),
    path('post/', include('post.urls')),
    path('accounts/', include('accounts.urls')),
]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

#urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

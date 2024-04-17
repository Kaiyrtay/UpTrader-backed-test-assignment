from django.contrib import admin
from django.urls import path, include
# include static files path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('menu_bar.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

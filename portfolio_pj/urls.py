from django.contrib import admin
from django.urls import path, include
from portfolio_app import views as portfolio_app_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('djoser.urls')),
    path('api/v1/', include('djoser.urls.authtoken')),
    path('api/v1/projects/', include('portfolio_app.urls')),
    path('', portfolio_app_views.AllProjectsView.as_view()), 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

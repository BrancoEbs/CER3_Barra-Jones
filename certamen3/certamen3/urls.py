from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('core/', include('core.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='core:home'), name='logout'), 
    path('', include('core.urls')),
]

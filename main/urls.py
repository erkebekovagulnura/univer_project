from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.users.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('subjects/', include('apps.Subject.urls')),
    path('tasks/', include('apps.Task.urls')),
    path('schedule/', include('apps.Shcedule.urls')),
]

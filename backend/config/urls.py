from django.contrib import admin
from rest_framework import routers
from django.urls import path, include
from todo_app import views

# router = routers.DefaultRouter()
# router.register('todos/', TodoViewSet, basename='todos')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('todos/', views.TodoView.as_view())
    # path('', include(router.urls)),
]

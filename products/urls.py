from django.urls import path

from .views import ProductViewSet, UserApiView

urlpatterns = [
    path('products', ProductViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('products/<str:pk>', ProductViewSet.as_view({
        'get': 'retrieve',
        'post': 'update',
        'delete': 'destroy'
    })),
    path('user', UserApiView.as_view())
]
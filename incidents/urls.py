# urls.py
from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, IncidentViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'incidents', IncidentViewSet, basename='incident')

urlpatterns = [
    path('api/register/', UserViewSet.as_view({'post': 'create'}), name='register'),
    path('api/login/', UserViewSet.as_view({'post': 'login'}), name='login'),
    path('api/forgot-password/', UserViewSet.as_view({'post': 'forgot_password'}), name='forgot_password'),
    path('api/incidents/', IncidentViewSet.as_view({'post': 'create', 'get': 'list'}), name='incident-list'),
    path('api/incidents/<int:pk>/', IncidentViewSet.as_view({'put': 'update', 'get': 'retrieve'}), name='incident-detail'),
    path('api/incidents/search/<str:incident_id>/', IncidentViewSet.as_view({'get': 'search'}), name='incident-search'),
]

 


# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import UserViewSet, IncidentViewSet
# from rest_framework.authtoken import views as authtoken_views

# router = DefaultRouter()
# router.register(r'users', UserViewSet)
# # router.register(r'incidents', IncidentViewSet)
# router.register(r'incidents', IncidentViewSet, basename='incident') 

# urlpatterns = [
#     path('api/', include(router.urls)),
#     path('api-token-auth/', authtoken_views.obtain_auth_token, name='api_token_auth')
# ]

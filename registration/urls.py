from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('register/',views.register.as_view()),
    path('login/',views.login.as_view()),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
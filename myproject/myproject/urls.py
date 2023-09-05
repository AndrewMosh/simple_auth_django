from django.urls import path

from authentication.views import RegisterView, CustomTokenObtainPairView

urlpatterns = [
    path("api/token/", CustomTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/register/", RegisterView.as_view(), name="register"),
    # Добавьте другие URL-маршруты здесь
]

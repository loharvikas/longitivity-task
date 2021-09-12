from django.urls import path
from .views import UserAPIView, OrganisationAPIView

urlpatterns = [
    path("register/", UserAPIView.as_view(), name="register"),
    path("organisation/", OrganisationAPIView.as_view(), name="organisation")
]
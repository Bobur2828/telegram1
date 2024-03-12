from django.urls import path
from .views import SignUpView,VerifyView,ResetVerifyView
urlpatterns = [
    path('signup/', SignUpView.as_view()),
    path('verify/', VerifyView.as_view()),
    path('resend/', ResetVerifyView.as_view()),


]

from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
from .views import UserCreateView,UserActivateView, UserLoginView,UserLogoutView
urlpatterns = [
    
    path('users/', UserCreateView.as_view(), name='user-create'),
    path('api/users/activate/<uidb64>/<token>/', UserActivateView.as_view(), name='user-activate'),
    path('users/login/', UserLoginView.as_view(), name='user-login'),
    path('users/logout/', csrf_exempt(UserLogoutView.as_view()), name='user-logout'),
    # path('users/profile/', UserProfileView.as_view(), name='user-profile'),
    # path('users/change_password/', UserChangePasswordView.as_view(), name='user-change-password'),
    # path('send-otp/', SendOtpView.as_view(), name='send-otp'),
    # path('users/forgot_password/', UserForgotPasswordView.as_view(), name='user-forgot-password'),
    # path('users/test_token/', test_token, name='test_token'),
    # path('users/set_security_pin/', SetSecurityPinView.as_view(), name='set-security-pin'),
    # path('users/reset_security_pin/', ResetSecurityPinView.as_view(), name='reset-security-pin'),
]
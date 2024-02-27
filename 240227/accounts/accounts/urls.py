from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name= 'signup'),
    path('login/', views.login, name= 'login'),
    path('logout/', views.logout, name= 'logout'),
    path('profile/', views.profile, name= 'profile'),
]

# 1.3 'accounts/signup/'          : 회원가입
# 1.4 'accounts/login/'           : 로그인
# 1.5 'accounts/logout/'          : 로그아웃
# 1.6 'accounts/profile/'         : 프로필
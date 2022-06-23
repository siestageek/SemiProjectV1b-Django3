from django.urls import path
from . import views

urlpatterns = [
    # 127.0.0.1/join 요청시 member apps의 join함수가 처리함
    path('join/', views.join, name='join'),

    path('login/', views.login, name='login'),
    path('myinfo/', views.myinfo, name='myinfo'),
    path('logout/', views.logout, name='logout'),
]

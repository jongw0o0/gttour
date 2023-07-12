from django.urls import path

from . import views

app_name = 'tourlist'

urlpatterns = [
    # path('', views.index, name='index1'),
    path('1/', views.index1, name='index1'),
    path('/2/', views.index2, name='index2'),
    path('/3/', views.index3, name='index3'),
    # 상세정보 url 필요할듯
]
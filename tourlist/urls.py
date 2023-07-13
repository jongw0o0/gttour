from django.urls import path

from . import views

app_name = 'tourlist'

urlpatterns = [
    # path('', views.index, name='index1'),
    path('index1/', views.index1, name='index1'),
    path('index2/', views.index2, name='index2'),
    path('index3/', views.index3, name='index3'),
    # 상세정보 url 필요할듯
]
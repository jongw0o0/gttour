from django.urls import path

from . import views

app_name = 'tourlist'

urlpatterns = [
    # path('', views.index, name='index1'),
    path('1/', views.indexone, name='indexone'),
    path('/2/', views.indextwo, name='indextwo'),
    path('/3/', views.indexthree, name='indexthree'),
    # 상세정보 url 필요할듯
]
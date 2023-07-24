from django.urls import path

from . import views

app_name = 'tourlist'

urlpatterns = [
    # path('', views.index, name='index1'),
    path('similadest_view/', views.similadest_view, name='similadest_view'),
    path('destination_view/', views.destination_view, name='destination_view'),
    # 상세정보 url 필요할듯
]
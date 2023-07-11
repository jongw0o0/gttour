from django.urls import path

from . import views

app_name = 'tourlist'

urlpatterns = [
    path('', views.index, name='index'),
    # 상세정보 url 필요할듯
]
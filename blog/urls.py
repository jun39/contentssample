from django.urls import path
from . import views
#パス関数をインポートして、同じディレクトリ内にあるviewsをインポートする
urlpatterns = [
    path('', views.post_list, name='post_list'),
]
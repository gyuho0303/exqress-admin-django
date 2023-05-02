from django.urls import path
from . import views

urlpatterns = [
    #BASIC URL --> localhost:8000/info/
    path('', views.main, name='main'),
    # 입력 요청 처리
    path('createInfo/', views.createInfo),
    # 수정페이지 요청 -> http://localhost:8000/info/edit/1
    path('edit/<int:idx>', views.editForm),
    path('edit/update/', views.updateInfo),
    path('delete/<int:idx>', views.deleteInfo),
]
from django.urls import path

from . import views

urlpatterns = [
    path('create/', views.ProductCreateAPIView.as_view()),
    path('', views.ProductListAPIView.as_view()),
    path('<int:pk>/', views.ProductDetailsAPIView.as_view()),
]
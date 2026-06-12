from django.urls import path

from . import views

urlpatterns = [
    path('create/', views.ProductCreateAPIView.as_view()),
    path('list/', views.ProductListAPIView.as_view()),
    path('', views.ProductListCreateAPIView.as_view()),
    path('<int:pk>/', views.ProductDetailsAPIView.as_view()),
]
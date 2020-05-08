from django.urls import path

from . import views

app_name = 'bacon'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/orders/', views.OrdersView.as_view(), name='orders'),
    path('place_order/', views.place_order, name='place_order'),
    path('<int:pk>/orders/order_again/', views.order_again, name='order_again')
]
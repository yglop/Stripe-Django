from django.contrib import admin
from django.urls import path

from main import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home),
    path('buy/<int:id>/', views.buy_item),
    path('item/<int:id>/', views.get_item),
    path('success/', views.success),
]

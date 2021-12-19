from django.urls import path
from . import views

urlpatterns = [
  path('',views.home,name="home"),
  path('post_data',views.post_data,name="post_data"),
  path('show/<int:id>',views.show,name="show")
]
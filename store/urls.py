from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('/category/<ctg_name>', views.category_post, name="category-post")
]
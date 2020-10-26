from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('category/<ctg_name>', views.category_post, name="category-post"),
    path('signup', views.signup, name="signup"),
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),
    path('cart', views.add_cart, name="cart")
]
from django.urls import path

from FarmerFruitsShop import views

urlpatterns = [
    path('',views.home),
    path('signin',views.signin_fun,name='signin'),
    path('login',views.login_fun,name='login'),
    path('product',views.product_fun,name='product'),
    path('location',views.location_fun,name='location'),
    path('movement',views.movement_fun,name='movement'),
    path('logout',views.logout_fun,name='logout'),
    path('add_fruit/',views.add_fruit,name='add_fruit'),
    path('add_location/',views.add_location,name='add_location'),
    path('add_movement/',views.add_movement,name='add_movement'),
    path('delete_movement/<int:id>/',views.delete_movement,name='delete_movement'),
    path('edit_fruit/<int:id>/', views.edit_fruit, name='edit_fruit'),
    path('edit_location/<int:id>/', views.edit_location, name='edit_location'),
    path('edit_movement/<int:id>/', views.edit_movement, name='edit_movement'),

]
from django.urls import path
from myapp.views import index,detail,cart_view,order,return_view,cancel_view
app_name='myapp'

urlpatterns = [
 path('',index,name='index'),
 path('<int:product_id>/<slug:slug>',detail,name='detail'),
 path('cart/',cart_view,name='cart_view'),
 path('order/',order,name='order'),
 path('sucess/',return_view,name='return_view'),
 path('cancel/',cancel_view,name='cancel_view'),
 
]
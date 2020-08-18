from django.urls import path
from. import views

urlpatterns=[
    path('',views.index),
    path('login',views.login),
    path('signup',views.add_staff),
    path('add',views.save_detail),
    path('category',views.add_category),
    path('save_category',views.save_category),
    path('rooms',views.rooms),
    path('save_room',views.save_room),
    path('savedata',views.saveprofile),
    path('addbook',views.addbook),
    path('dataadd',views.dataadd),
    path('addservice',views.addservice),
    path('services',views.services),
    path('custservice',views.custservice),
    path('addservice_cust',views.addservice_cust),
    path('customerview',views.customerview),
    path('bill/<int:id>',views.bill),
    path('del/<int:id>',views.delete)
    
] 
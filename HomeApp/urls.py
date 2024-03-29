from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.homeview, name='home'), 
    
    path('back_home/',views.back_home,name='back_home'),


    path('home_customer_view',views.home_customer_view,name='home_customer_view'),
    path('redirectRegister',views.controller_redirect_register, name='redirectRegister'),
    path('handle_logout',views.handle_logout,name='handle_logout'),
    path('controller_redirect_regisCustomer',views.controller_redirect_regisCustomer, name='controller_redirect_regisCustomer'),
    path('driver_login_view/',views.driver_login_view,name='driver_login_view'),

    path('checkBeforeBook/<int:schedule_id>/<int:customer_id>/<int:slots>/',views.checkBeforeBook,name='checkBeforeBook'),
    path('handle_book_vehicle_second/<int:schedule_id>/<int:customer_id>/<int:slot>/',views.handle_book_vehicle_second,name='handle_book_vehicle_second'),
    path('book_vehicle/<int:schedule_id>/<int:customer_id>/<int:slot>/',views.handle_book_vehicle,name='handle_book_vehicle'),

    path('handle_cancel_order/<int:idorder>/',views.handle_cancel_order,name='handle_cancel_order'),
    
    path('search_customer/',views.search_customer, name='search_customer'),
    path('search_datetime_and_word/',views.search_datetime_and_word, name='search_datetime_and_word'),

    path('search_home/',views.search_home, name='search_home'),
    path('view_profile_customer',views.view_profile_customer,name='view_profile_customer'),
    path('view_editprofile',views.view_editprofile,name='view_editprofile'),
    path('upload_images/<int:customerid>/',views.upload_images,name='upload_images'),
    path('save_edit_info/',views.save_edit_info,name='save_edit_info'),
    path('custom_logout/',views.custom_logout, name='custom_logout'),

    path('send_otp_sms/',views.send_otp_sms, name='send_otp_sms'),
    path('handelOTP/',views.handelOTP,name='handelOTP'),
    path('save_edit_phone/',views.save_edit_phone,name='save_edit_phone'),

    path('view_change_pass/',views.view_change_pass, name ='view_change_pass'),
    path('check_pass_customer/',views.check_pass_customer, name ='check_pass_customer'),
    path('handle_change_pass/',views.handle_change_pass, name ='handle_change_pass'),
]

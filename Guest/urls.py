from django.urls import path
from . import views

urlpatterns=[
    path('',views.homepage),
    path('login',views.login),
    path('signup',views.signup),
    path('signout',views.signout),
    path('showrooms/<id>',views.showrooms),
    path('viewdetails/<id>',views.viewdetails),
    path('searchavailability',views.searchavailability),
    path('booknow',views.booknow),
    path('makepayment',views.makepayment),
    path('payment',views.payment),
    path('mybooking',views.mybooking),
]
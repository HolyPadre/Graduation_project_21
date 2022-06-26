from django.urls import path


from .views import (  CustomAuthToken, CustomerSignupView, LogoutView, CustomerOnlyView,VendorOnlyView,ManagerOnlyView, VendorSignupView , view_users)

urlpatterns=[
    path('signup/customer', CustomerSignupView.as_view()),
    path('signup/vendor', VendorSignupView.as_view()),
    path('login',CustomAuthToken.as_view(), name='auth-token'),
    path('logout', LogoutView.as_view(), name='logout-view'),
    path('customer/dashboard', CustomerOnlyView.as_view(), name='customer-dashboard'),
    path('vendor/dashboard', VendorOnlyView.as_view(), name='vendor-dashboard'),
    path('manager/dashboard', ManagerOnlyView.as_view(), name='manager-dashboard'),
    path('users', view_users, name='view-guests'),
]
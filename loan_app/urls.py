from django.conf.urls import url
from loan_app import views
from django.urls import path

app_name = 'loan_app'

urlpatterns =[
    path('login/',views.user_login,name='user_login'),
    path('signup/',views.signup,name='signup'),

]

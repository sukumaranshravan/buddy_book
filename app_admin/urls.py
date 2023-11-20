from django.urls import path
from . import views
from django.conf.urls.static import static
urlpatterns = [
    path('',views.start_up,name='start_up'),
    path('log_in/',views.log_in,name='log_in'),
    path('log_out/',views.log_out,name='log_out'),
    path('register/',views.register,name='register'),
]
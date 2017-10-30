from django.conf.urls import url,include
from . import views
from django.contrib.auth.views import login,logout


urlpatterns = [
    url(r'^$', views.user_login,name='welcome'),
    url(r'^login/$', views.user_login,name='login'),
    url(r'^logout/$', views.user_logout,name='logout'),
    url(r'^in/$', views.user_in,name='in'),
    url(r'^invalid/$', views.user_invalid,name='invalid'),
    url(r'^register/$', views.user_register, name='register'),
    url(r'^reg_done/$', views.user_reg_done, name='reg_done'),
    url(r'^share/$', views.user_share, name='share'),
    url(r'^upload/$', views.user_upload, name='upload'),
    url(r'^delete/$', views.user_delete, name='delete'),
    url(r'^files/$', views.user_files_all, name='files'),
    url(r'^profile/$', views.user_profile, name='profile'),
]


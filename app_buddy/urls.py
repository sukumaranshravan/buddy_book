from django.urls import path
from . import views
from django.conf.urls.static import static
urlpatterns = [
    path('registeraction/',views.registeraction,name='registeraction'),
    path('my_post/',views.my_post,name='my_post'),
    path('home/',views.home,name='home'),
    path('post/',views.post,name='post'),
    path('postaction/',views.postaction,name='postaction'),
    path('find_buddy/',views.find_buddy,name='find_buddy'),
    path('comment<int:id>/',views.comment,name='comment'),
    path('commentaction/',views.commentaction,name='commentaction'),
    path('reply<int:id>/',views.reply,name='reply'),
    path('request_for_friendship/',views.request_for_friendship,name='request_for_friendship'),
    path('friend_request/',views.friend_request,name='friend_request'),
    path('accept<int:id>/',views.accept,name='accept'),
    path('reject<int:id>/',views.reject,name='reject'),
    path('friend_list/',views.friend_list,name='friend_list'),
    path('about_me/',views.about_me,name='about_me'),
    path('unfriend<int:id>/',views.unfriend,name='unfriend'),
    path('my_photos/',views.my_photos,name='my_photos'),
    path('settings/',views.settings,name='settings'),
    path('change_photo/',views.change_photo,name='change_photo'),
    path('delete_post<int:id>/',views.delete_post,name='delete_post'),
    path('likes<int:id>/',views.likes,name='likes'),
]

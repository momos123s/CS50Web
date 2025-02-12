
from django.urls import path
from django.conf.urls.static import static 
from django.conf import settings
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("new", views.new_post, name="new_post"),
    path("get_posts/<str:page_num>", views.get_posts, name="get_posts"),
    path("update_likes", views.update_likes, name="update_likes"),
    path("profile_view", views.profile_view, name="profile_view"),
    path("load_profiles",views.load_profiles,name="load_profiles"),
    path("follow",views.follow_view, name="follow"),
    path("followOrUnfollow",views.follow_posts, name="followOrUnfollow"),
    path("update_descr", views.edit_description,name="update_descr")
]

urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)


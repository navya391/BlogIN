from django.urls import path
from . import views

urlpatterns=[
    path('', views.home, name='home'),
    path('base', views.base, name='base'),
    path('signup',views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('base/blogadd', views.blogadd, name='blogadd'),
    path('signin/category', views.category, name='category'),
    path('post', views.post, name='post'),
    path('fullpost/<str:pk>', views.fullpost, name='fullpost'),
    path('base/addprofile', views.addprofile, name="addprofile"),
    path('signout', views.signout, name="signout"),
    path('search', views.search, name="search"),
    path('base/viewprofile', views.viewprofile, name='viewprofile'),
    path('filter_category/<str:pk>', views.filter_category, name='filter_category'),
    path('base/editblog/<int:id>', views.editblog,name="editblog"),
    path('base/deleteblog/<int:id>',views.deleteblog, name='deleteblog'),
    path('like/<int:id>' , views.like, name="like"),
    path('dislike/<int:id>', views.dislike, name="dislike"),
    path('bloggers', views.bloggers, name="bloggers"),
    path('fullprofile/<str:pk>', views.fullprofile, name='fullprofile'),
    path('base/editprofile/<int:id>', views.editprofile, name='editprofile'),
    path('base/deleteprofile/<int:id>',views.deleteprofile, name='deleteprofile'),

]
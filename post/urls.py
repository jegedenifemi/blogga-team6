from django.urls import path
from post import views
from django.contrib.auth import views as auth_views
from accounts.forms import PwdChangeForm
app_name='post'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.createPost, name = 'create_post'),
    path('post/<slug:slug>/', views.postDetail, name='post_detail'),
    path('post/<slug:slug>/delete/', views.postDelete, name ='post_delete'),
    path('post/<slug:slug>/update/', views.update, name ='post_update'),
    path('category/<str:category_slug>', views.category_view, name = 'post_category'),
    path('contents/', views.contents, name='content'),
    path('bookmarks/', views.bookmarks, name = 'bookmarks'),
    path('archive/', views.archive_view, name='archive'),
    path('our-team/', views.team_view, name='our-team'),
    path('privacy-policy/', views.privacy_view, name ='privacy-policy'),
    path('profile/',auth_views.PasswordChangeView.as_view(template_name='raw/profilepage.html',
                                                form_class =PwdChangeForm), name='profile'),
    path('terms/',views.terms_view, name='terms'),
    path('content/', views.contents),
    path('write-for-us/', views.write)
    
]
# {% url 'app_name:url_name' %}
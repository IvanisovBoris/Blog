from django.urls import path
from . import views

urlpatterns = [
#    path('', views.ArticleListView.as_view(), name='home'),
#    path('article/<int:pk>', views.ArticleDetailView.as_view(), name='detail'),
#    path('', views.index, name='index'),
    path('article/<int:article_id>/', views.article_detail, name='article'),
    path('all_reviews/', views.all_reviews, name='all_reviews'),
    path('all_articles/', views.all_articles, name='all_articles'),
    path('login_view/', views.login_view, name='login_view'),
    path('logout_view/', views.logout_view, name='logout_view'),
]







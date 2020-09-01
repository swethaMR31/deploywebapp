from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [

   # path('login/', auth_views.LoginView.as_view(), name='login'),
    path('', views.index,name='index'),
    path('logout', views.logout, name='logout'),
    path('main/', views.main, name='main'),
    path('candidate/', views.candidate.as_view(), name='candidate'),
    path('register/', views.register, name='register'),
    path('profile', views.profilepage, name='profile'),
    path('list',views.List.as_view()),
   # path('edit/<int:id>', views.edit),
    path('<pk>/update', views.Update.as_view()),
    path('<pk>/delete', views.Delete.as_view()),


    path('coach/', views.Coach_create.as_view(), name='coach'),
    path('coach_list', views.Coach_List.as_view()),
    # path('edit/<int:id>', views.edit),
    path('<pk>/coach_update', views.Coach_Update.as_view()),
    path('<pk>/coach_delete', views.Coach_Delete.as_view()),

]




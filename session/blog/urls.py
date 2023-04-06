from django.urls import path
from . import views

urlpatterns = [
    # path('', views.login_v, name='login'),
    path('<str:user_name>/blog/', views.home, name='home'),
    path('<str:user_name>/blog/<int:blog_id>/', views.detail, name='detail'),
    path('<str:user_name>/blog/new/', views.new, name='new'),
    path('<str:user_name>/blog/create/', views.create, name='create'),
    path('<str:user_name>/blog/edit/<int:blog_id>/', views.edit, name="edit"),
    path('<str:user_name>/blog/update/<int:blog_id>/',
         views.update, name="update"),
    path('<str:user_name>/blog/delete/<int:blog_id>/',
         views.delete, name="delete"),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_v, name='login'),
    path('<str:user_name>/blog/blog_search/', views.blog_search, name='blog_search'),
    path('logout/', views.logout_v, name='logout'),
]

# urlpatterns = [
#     path('', views.login_v, name='login'),
#     path('blog/', views.home, name='home'),
#     path('blog/<int:blog_id>',views.detail,name='detail'),
#     path('blog/new',views.new,name='new'),
#     path('blog/create',views.create,name='create'),
#     path('blog/edit/<int:blog_id>', views.edit, name="edit"),
#     path('blog/update/<int:blog_id>', views.update, name="update"),
#     path('blog/delete/<int:blog_id>', views.delete, name="delete"),
#     path('signup/', views.signup, name='signup'),
#     path('login/', views.login_v, name='login'),
#     path('logout/', views.logout_v, name='logout'),
# ]

from django.contrib import admin
from django.urls import path, include
from blog import views
# from django.shortcuts import redirect

# def handle_unknown_urls(request):
#     return redirect('')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    # path('signup/', views.signup, name='signup'),
    # path('login/', views.login_v, name='login'),
    # path('logout/', views.logout_v, name='logout'),
]

# urlpatterns += [
#     path('<path:url>', handle_unknown_urls)
# ]
# 127.0.0.1:8000/blog
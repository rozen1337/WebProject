from datetime import datetime
from django.urls import path, re_path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from app import forms, views


urlpatterns = [
    path('', views.home, name='home'),
    path('blog/', views.blog, name='blog'),
    re_path(r'^(?P<parametr>\d+)/$', views.article, name='article'),
    path('links/', views.links, name='links'),
    path('feedback/', views.feedback, name='feedback'),
    path('videopost/', views.videopost, name='videopost'),
    path('about/', views.about, name='about'),
    path('newpost/', views.newpost, name='newpost'),
    path('register/', views.registration, name='register'),
    path('login/',
         LoginView.as_view
         (
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Авторизация',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()

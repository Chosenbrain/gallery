"""gallery URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings 
from django.conf.urls.static import static 

from website import views




urlpatterns = [
    path('', views.photos_view, name='photos'),
    path('patios/<int:id>', views.pic_detail, name='pic_detail'),
    path('resins/<int:id>', views.res_detail, name='res_detail'),
    path('tarmac/<int:id>', views.tam_detail, name='tam_detail'),
    path('fencing/<int:id>', views.fen_detail, name='fen_detail'),
    path('blockpaving/<int:id>', views.bap_detail, name='bap_detail'),
    path('wall/<int:id>', views.wa_detail, name='wa_detail'),
    path('blog/', views.blog, name='blog'),
    path('bio/', views.bio, name='bio'),
    path('quotes/', views.quotes, name='quotes'),
    path('admin/', admin.site.urls)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


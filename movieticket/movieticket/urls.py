from django.contrib import admin
from django.urls import path
from movieapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('upcoming/',views.upcoming),
    path('index/upcoming/',views.upcoming),
    path('login/',views.login),
    path('signup/',views.signup),
    path('booked/',views.booked),
    path('index/',views.index),
    path('about/',views.about),
    path('index/about/',views.about),
    path('details/<int:id>/',views.details),
    path('index/details/<int:id>/',views.details),
    path('updetails/<int:id>/',views.updetails),
    path('index/updetails/<int:id>/',views.updetails),
    path('aboutmore/',views.aboutmore)
]
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 

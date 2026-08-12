
from django.urls import path
from . import views
from django.urls import path
from . import views

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('verses/', views.verses, name='verses'),
    path('mawlid/', views.mawlid, name='mawlid'),
    path('seerah/', views.seerah, name='seerah'),
    path('sahaba/', views.sahaba, name='sahaba'),
    path('ahlalbayt/', views.ahlalbayt, name='ahlalbayt'),
    path('hadith/', views.hadith, name='hadith'),
    path('videos/', views.videos, name='videos'),
]
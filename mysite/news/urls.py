from django import urls
from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('articles/<int:year>/',views.year_archive),
    #path('articles/<int:year>/<int:month>/',views.month_archive),
    #path('articles/<int:year>/<int:month>/<int:pk>',views.article_detail),
    path('',views.index,name='index')
]
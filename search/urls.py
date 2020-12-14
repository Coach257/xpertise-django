from django.urls import path

from . import views

urlpatterns =[
    path('',views.index,name='index'),
    path('api/v1/search_author',views.search_author,name='search_author'),
    path('api/v1/search_paper',views.search_paper,name='search_paper')
]
from django.urls import path
from .views import index,create,delete,search,confirm


urlpatterns=[
    path('',index),
    path('create/',create),
    path('delete/<str:id>/',delete),
    path('search/',search),
    path('search/confirm/',confirm)
]
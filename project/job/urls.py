from django.urls import path
from .views import JobActiveList,JobCreate,index,JobSelectedList




urlpatterns=[
    path('list/',JobActiveList.as_view(),name='jobactivelist'),
    path('job/',JobSelectedList.as_view(),name='jobselectedlist'),
    path('',index,name='index'),
    path('create/',JobCreate.as_view(),name='jobcreate')
]

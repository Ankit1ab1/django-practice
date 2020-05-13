from django.shortcuts import render
from rest_framework import generics
from .serializers import JobSerializers
from .models import JobModel
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import  OrderingFilter,SearchFilter

# Create your views here.
def index(request):
    return render(request,'job/index.html')

class JobActiveList(generics.ListAPIView):
    serializer_class=JobSerializers
    queryset=JobModel.objects.filter(is_active=True)


class JobSelectedList(generics.ListAPIView):
    serializer_class=JobSerializers
    queryset=JobModel.objects.all()
    filter_backends=(DjangoFilterBackend,OrderingFilter)
    filter_fields=('job_title','location','is_active')
    ordering_fields=('salary','location')

    
class JobCreate(generics.CreateAPIView):
    serializer_class=JobSerializers
   
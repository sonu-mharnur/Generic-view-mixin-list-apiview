from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Course
from rest_framework import status
from django .http import Http404
from .serializers import CourseSerializer
from rest_framework import mixins,generics




# ListAPIViews.Generics Method

class CourseListView(generics.ListAPIView,generics.CreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer



class CourseDetailview(generics.RetrieveAPIView,generics.UpdateAPIView,generics.DestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer




## GENETRIC VIEWS 

class CourseListView(mixins.ListModelMixin,mixins.CreateModelMixin ,generics.GenericAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    def get(self,request):
        return self.list(request)
    
    def post(self,request):
        return self.create(request)
    
class CourseDetailview(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk)

    def put(self, request, pk):
        return self.update(request, pk)
            
    def delete(self, request, pk):
        return self.destroy(request, pk)

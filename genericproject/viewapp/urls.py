from django.urls import path
# from .views import CourseListView, CourseDetailview # Assuming your view class is named CourseListView
from .import views
urlpatterns = [
    path('courselist/',views.CourseListView.as_view(), name='home'),  # Note: Added '/' to the URL path
    path('courselist/<int:pk>/',views.CourseDetailview.as_view(), name='home'),
]
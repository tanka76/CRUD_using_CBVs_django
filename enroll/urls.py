from django.contrib import admin
from django.urls import path
from enroll import views

urlpatterns = [
   
    #path('',views.addshow,name="addandshow"),
    path('',views.addshowview.as_view(),name="addandshow"),
    path('delete/<int:id>/',views.userdelete.as_view(),name="deletedata"),
    path('<int:id>/',views.userview.as_view(),name="updatedata"),

]

from django.urls import path
from .views import TeamList,AddPeople,EditPeople,DeletPeople

urlpatterns = [
   path('',TeamList.as_view(),name='team'),
   path('add-people/',AddPeople.as_view(),name="add-people"),
   path('edit-people/<int:pk>',EditPeople.as_view(),name='edit-people'),
   path('delete-people/<int:pk>',DeletPeople.as_view(),name='delete-people'),
   


]


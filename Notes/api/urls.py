from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview,  name= 'api-overview'),
    path('notes-list/' , views.NotesList, name='notes-list'),
    path('note-details/<str:pk>/' , views.NoteDetails, name='note-details'),
    path('create-note/', views.CreateNote, name='create-not'),
    path('update-note/<str:pk>/',views.UpdateNote,name='update-note'),
    path('delete-note/<str:pk>/',views.DeleteNote,name='delete-note'),
    
]
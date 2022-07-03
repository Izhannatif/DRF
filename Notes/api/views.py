from urllib import response
from django.shortcuts import render
from django.http import JsonResponse
from .models import Note
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import NoteSerializer
from .models import Note
@api_view(['GET'])
def apiOverview(request):
    return Response("API Base safe Point" , safe=False)

@api_view(['GET'])
def NotesList(request):
    notes = Note.objects.all()
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def NoteDetails(request,pk):
    note = Note.objects.get(id=pk)
    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def CreateNote(request):
    serializer = NoteSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def UpdateNote(request,pk):
    note = Note.objects.get(id=pk)
    serializer = NoteSerializer(instance=note ,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def DeleteNote(request,pk):
    note = Note.objects.get(id=pk)
    note.delete()
    return Response('Deleted Successfully!')  

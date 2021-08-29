from django.shortcuts import render
from core import serializers
from core.models import Project
from core.serializers import ProjectSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

def home(request):
    context = {'texto': 'Project with Django Started By Maciel Serafim!!!!'}
    return render(request, 'index.html', context)


# APIs - Prepared to statup service
@api_view(['GET'])
def ProjectList(request):
    list = Project.objects.all()
    serialized = ProjectSerializer(list, many=True)
    return Response(serialized.data)


@api_view(['POST'])
def ProjectPost(request):
    proj = ProjectSerializer(data=request.data)
    if proj.is_valid():
        proj.save()
        return Response(proj.data)
    return Response(proj.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def ProjectPut(request, pk):
    proj = Project.objects.get(id=pk)
    serialized = ProjectSerializer(proj, data=request.data)
    if serialized.is_valid():
        serialized.save()
        return Response(pk)
    return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def ProjectDel(request, pk):
    proj = Project.objects.get(id=pk)
    proj.delete()
    return Response('OK')

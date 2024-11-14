from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Todo
from .serializer import TodoSerializer


@api_view(['GET'])
def GetData(request):
    
    data = Todo.objects.all()
    serializer = TodoSerializer(data, many=True)
    jsonData = serializer.data
    return Response(jsonData)


@api_view(['POST'])
def SetData(request):
    
    serializer = TodoSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)

@api_view(['DELETE'])
def DeleteData(request, pk):
    
    item = Todo.objects.get(id=pk)
    item.delete()
    
    return Response('Item deleted')

@api_view(['PUT'])
def CheckData(request, pk):
    
    item = Todo.objects.get(id=pk)
    
    item.completed = not item.completed
    item.save()
    
    return Response('item checked')
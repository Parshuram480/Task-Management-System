from rest_framework import permissions, status
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from usertask.models import AddTask
from .serializers import RegisterSerializer, TaskSerializer, AddTaskSerializer


@api_view(['POST'])
def register_api(request):
    serializer = RegisterSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'user created successfully', 'user': serializer.data}, status=201)
    return Response(serializer.errors, status=400)


@api_view(['POST'])
def login_api(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(username=username, password=password)
    if user is not None:
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'message': 'user created successfully', 'token': token.key}, status=200)
    return Response({'error': 'invalid credentialS'}, status=401)


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def logout_api(request):
    request.user.auth_token.delete()
    return Response({"message": "Successfully logged out."}, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def task_list_api(request):
    tasks = AddTask.objects.filter(user=request.user)
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def add_task_api(request):
    serializer = AddTaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response({'message': 'Task added successfully', 'task': serializer.data}, status=201)
    return Response(serializer.error, status=400)


@api_view(['PUT'])
@permission_classes([permissions.IsAuthenticated])
def update_task_api(request, task_id):
    task = AddTask.objects.filter(id=task_id, user=request.user).first()
    if not task:
        return Response({'error': 'Task Not Found'}, status=404)

    serializer = AddTaskSerializer(task, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Task updated successfully', 'task': serializer.data}, status=201)
    return Response(serializer.errors, status=400)


@api_view(['DELETE'])
@permission_classes([permissions.IsAuthenticated])
def delete_task_api(request, task_id):
    task = AddTask.objects.filter(id=task_id, user=request.user).first()
    if not task:
        return Response({'error': 'Task Not Found'}, status=404)
    task.delete()
    return Response({'message': 'Task deleted Successfully'}, status=204)


@api_view(['PATCH'])
@permission_classes([permissions.IsAuthenticated])
def toggle_task_api(request, task_id):
    task = AddTask.objects.filter(id=task_id, user=request.user).first()
    if not task:
        return Response({'error': 'Task Not Found'}, status=404)
    task.status = not task.status
    task.save()
    return Response({'message': 'status upadated'}, status=200)

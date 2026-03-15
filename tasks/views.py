from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Task
from .serializers import TaskSerializer, UserRegistrationSerializer, UserProfileSerializer

# Authentication Views
@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    serializer = UserRegistrationSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        return Response({
            'user': UserProfileSerializer(user).data,
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    
    try:
        user = User.objects.get(username=username)
        if user.check_password(password):
            refresh = RefreshToken.for_user(user)
            return Response({
                'user': UserProfileSerializer(user).data,
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    except User.DoesNotExist:
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def profile(request):
    serializer = UserProfileSerializer(request.user)
    return Response(serializer.data)

# Task Views
class TaskListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer
    
    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def update_task_status(request, pk):
    """Update only the status of a specific task"""
    try:
        task = Task.objects.get(pk=pk, user=request.user)
    except Task.DoesNotExist:
        return Response({'error': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)
    
    new_status = request.data.get('status')
    if not new_status:
        return Response({'error': 'Status field is required'}, status=status.HTTP_400_BAD_REQUEST)
    
    # Validate status
    valid_statuses = [choice[0] for choice in Task.STATUS_CHOICES]
    if new_status not in valid_statuses:
        return Response({
            'error': f'Invalid status. Must be one of: {valid_statuses}'
        }, status=status.HTTP_400_BAD_REQUEST)
    
    task.status = new_status
    task.save()
    
    serializer = TaskSerializer(task)
    return Response(serializer.data)

class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer
    
    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

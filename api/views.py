from .serializers import UserSerializer, RegisterSerializer, PostSerialization, CommentSerialization, UpsSerialization
from .models import Post, Comments, Up
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import viewsets
from django.db.models import F


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        # ...

        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class UserDetailAPI(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        user = User.objects.get(id=request.user.id)
        serializer = UserSerializer(user)
        return Response(serializer.data)


class RegisterUserAPIView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

# POSTS
# POSTS
# POSTS


@api_view(['GET'])
def getPosts(request, format=None):
    post = Post.objects.all().order_by('-id')
    serializer = PostSerialization(post, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getPost(request,id):
    post = Post.objects.get(id=id)
    serializer = PostSerialization(post)
    return Response(serializer.data)


@api_view(['POST'])
def addPosts(request, format=None):
    serializer = PostSerialization(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(["GET"])
def updatePosts(request, pk, userIdUp):
    post = Post.objects.get(id=pk)
    serializer = PostSerialization(
        post.ups.add(Up.objects.get(username=userIdUp)))
    return Response(serializer.data)


@api_view(["GET"])
def addComment(request,commentId, pk):
    post = Post.objects.get(id=pk)
    serializer = PostSerialization(
        post.comments.add(commentId)) #send id of comment that you created
    return Response(serializer.data)

# POSTS
# POSTS
# POSTS


# comments
# comments
# comments
@api_view(['GET'])
def getComments(request, format=None):
    up = Comments.objects.all()
    serializer = CommentSerialization(up, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getComment(request,id, format=None):
    up = Comments.objects.get(id=id)
    serializer = CommentSerialization(up)
    return Response(serializer.data)
    
@api_view(['POST'])
def addCommentField(request):
    serializer = CommentSerialization(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
# comments
# comments
# comments


# UPS
# UPS
# UPS


@api_view(['GET'])
def getUps(request, format=None):
    up = Up.objects.all()
    serializer = UpsSerialization(up, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def addPostUp(request):
    serializer = UpsSerialization(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# UPS
# UPS
# UPS

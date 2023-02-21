from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path("get-details/", views.UserDetailAPI.as_view()),
    path('register/', views.RegisterUserAPIView.as_view()),
    path('api/token/', views.MyTokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # POSTS
    path('getPosts/', views.getPosts),
    path('getPost/<int:id>', views.getPost),
    path('addPosts/', views.addPosts),
    path('addComment/<int:pk>/<int:commentId>', views.addComment),
    path('updatePosts/<int:pk>/<str:userIdUp>', views.updatePosts),
    # POSTS

    # UPS
    path('addPostUp/', views.addPostUp),
    path('getUps/', views.getUps),
    # UPS

    # comments
    path('getComments/', views.getComments),
    path('getComment/<int:id>', views.getComment),
    path('addCommentField/', views.addCommentField),
    # comments
]

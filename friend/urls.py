from django.urls import path

from .views import AcceptFriendRequestView, RejectFriendRequestView, SendFriendRequestView, FriendListView

urlpatterns = [
    path('api/accept_request/<str:request_id>', AcceptFriendRequestView.as_view(), name='accept_request'),
    path('api/reject_request/<str:request_id>', RejectFriendRequestView.as_view(), name='reject_request'),    
    path('api/send_request/<str:user_id>', SendFriendRequestView.as_view(), name='send_request'),
    path('api/friends/', FriendListView.as_view(), name='friend_list'),
    path('api/pending_friends/', FriendListView.as_view(), name='pending_friend_list'),
]

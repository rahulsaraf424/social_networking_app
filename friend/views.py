from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User

from .models import Friend

class SendFriendRequestView(APIView):

    permission_classes = (IsAuthenticated,)

    def post(self, request, user_id):
        from_user = request.user
        to_user = User.objects.get(id=user_id)
        friend_req, created = Friend.objects.get_or_create(from_user=from_user, to_user=to_user)
        if created:
            return Response('Firend request sent successfully', status=status.HTTP_201_CREATED)
        return Response('Friend request was already sent', status=status.HTTP_409_CONFLICT)


class AcceptFriendRequestView(APIView):

    permission_classes = (IsAuthenticated,)

    def post(self, request, request_id):
        try:
            friend_req = Friend.objects.get(id=request_id)
            if friend_req.to_user == request.user:
                friend_req.accept()
                friend_req.save()
                return Response('Friend request accepted', status=status.HTTP_202_ACCEPTED)
        except ObjectDoesNotExist:
            return Response('Error')


class RejectFriendRequestView(APIView):

    permission_classes = (IsAuthenticated,)

    def post(self, request, request_id):
        try:
            friend_req = Friend.objects.get(id=request_id)
            if friend_req.to_user == request.user:
                friend_req.reject()
                friend_req.save()
                return Response('Friend request rejected')
        except ObjectDoesNotExist:
            return Response('Error')


class FriendListView(APIView):

    permission_classes = (IsAuthenticated,)

    def get(self, request):
        user = request.user
        friend = Friend.objects.filter(to_user=user.id, state='accept')
        return Response([f.from_user.username for f in friend], status=status.HTTP_200_OK)


class PendingFriendListView(APIView):

    permission_classes = (IsAuthenticated,)

    def get(self, request):
        user = request.user
        friend = Friend.objects.filter(to_user=user.id, state='send')
        return Response([f.from_user.username for f in friend], status=status.HTTP_200_OK)

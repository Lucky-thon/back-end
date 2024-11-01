# notification/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Notification
from .serializers import NotificationSerializer

class NotificationListAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        notifications = request.user.notifications.filter(is_read=False)
        serializer = NotificationSerializer(notifications, many=True)
        return Response(serializer.data)

    def put(self, request):
        notifications = request.user.notifications.filter(is_read=False)
        notifications.update(is_read=True)
        return Response({"message": "All notifications marked as read"}, status=status.HTTP_200_OK)

class UnreadNotificationCheckAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # 읽지 않은 알림이 있는지 여부를 확인
        has_unread_notifications = Notification.objects.filter(user=request.user, is_read=False).exists()
        return Response({"has_unread_notifications": has_unread_notifications})
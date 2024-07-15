from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.db.models import Count
from django.db.models.functions import TruncDate
from .models import Follow
from .serializers import FollowSerializer, DailyFollowersSerializer, GetAllUsersSerializer


class FollowUserView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = FollowSerializer

    def create(self, request, *args, **kwargs):
        follower = request.user
        following_id = kwargs.get('user_id')
        
        try:
            following = User.objects.get(id=following_id)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        
        if Follow.objects.filter(follower=follower, following=following).exists():
            return Response({'error': 'Already following'}, status=status.HTTP_400_BAD_REQUEST)
        
        if follower == following:
            return Response({'error': 'user can not follow itself'}, status=status.HTTP_400_BAD_REQUEST)
        
        follow = Follow.objects.create(follower=follower, following=following)
        serializer = self.get_serializer(follow)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UnfollowUserView(generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer

    def delete(self, request, *args, **kwargs):
        follower = request.user
        following_id = kwargs.get('user_id')
        
        try:
            following = User.objects.get(id=following_id)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        
        follow = Follow.objects.filter(follower=follower, following=following)
        if not follow.exists():
            return Response({'error': 'Not following'}, status=status.HTTP_400_BAD_REQUEST)
        
        follow.delete()
        return Response({'success': 'Unfollowed successfully'}, status=status.HTTP_200_OK)



class DailyFollowersView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = DailyFollowersSerializer

    def get_queryset(self):
        followers_per_day = (
            Follow.objects.annotate(date=TruncDate('created_at'))
            .values('date', 'following')
            .annotate(count=Count('follower', distinct=True))
        )
        return followers_per_day

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        daily_followers = {}
        for entry in queryset:
            date = entry['date']
            count = entry['count']
            if date in daily_followers:
                daily_followers[date] += count
            else:
                daily_followers[date] = count

        result = [{'date': date, 'count': count} for date, count in daily_followers.items()]
        return Response(result)
    

class GetUsersView(generics.ListAPIView):
    serializer_class = GetAllUsersSerializer
    queryset = User.objects.all()



class CommonFollowersView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = GetAllUsersSerializer

    def get_queryset(self):
        user1 = self.request.user
        user2_id = self.kwargs.get('user2_id')

        try:
            user2 = User.objects.get(id=user2_id)
        except User.DoesNotExist:
            return User.objects.none() 

        user1_followers = Follow.objects.filter(follower=user1).values_list('following', flat=True)

        user2_followers = Follow.objects.filter(follower=user2).values_list('following', flat=True)

        common_followers = User.objects.filter(id__in=user1_followers).filter(id__in=user2_followers)

        return common_followers

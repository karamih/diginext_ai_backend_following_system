from django.urls import path
from .views import FollowUserView, UnfollowUserView, DailyFollowersView, GetUsersView, CommonFollowersView

urlpatterns = [
    path('user/<int:user_id>/follow', FollowUserView.as_view(), name='follow-user'),
    path('user/<int:user_id>/unfollow', UnfollowUserView.as_view(), name='unfollow-user'),
    path('user/daily-followers', DailyFollowersView.as_view(), name='daily-followers'),
    path('user/users', GetUsersView.as_view(), name='get-users'),
    path('user/<int:user2_id>/common-followers', CommonFollowersView.as_view(), name='common-followers')
]

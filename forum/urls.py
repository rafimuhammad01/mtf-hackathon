from django.urls import path
from forum.views import ForumList, ForumDetail, VoteForumIncrement, VoteAnswerIncrement

urlpatterns = [
    path('<int:id>/', ForumDetail.as_view(), name="forum_detail"),
    path("", ForumList.as_view()),
    path('<int:id>/vote', VoteForumIncrement.as_view()),
    path('answer/<int:id>/vote', VoteAnswerIncrement.as_view())
]
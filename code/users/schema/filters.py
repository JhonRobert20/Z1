from django_filters import FilterSet
from django_filters.filters import OrderingFilter
from django.db.models import Count
from ..models import User


class CustomOrderingFilter(OrderingFilter):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.extra['choices'] += [
            ('most_liked', 'Most likes'),
            ('most_followers', 'Most Followers'),
            ('posts_count', 'Posts count'),
        ]

    def filter(self, qs, value):
        if value:
            if 'most_liked' in value:
                return qs.annotate(likes_count=Count('likes')).order_by('-likes_count')

            if 'most_followers' in value:
                return qs.annotate(followers_count=Count('followers')).order_by('-followers_count')

            if 'posts_count' in value:
                return qs.annotate(posts_count=Count('posts')).order_by('-posts_count')

        return super().filter(qs, value)


class UserFilterSet(FilterSet):
    order_by = CustomOrderingFilter()

    class Meta:
        model = User
        fields = {
            'id': ['exact', 'icontains'],
            'date_joined': ['exact', 'gt', 'gte', 'lt', 'lte'],
            'email': ['exact', 'icontains'],
            'username': ['exact', 'icontains']
        }

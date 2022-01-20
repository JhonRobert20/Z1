from django_filters import FilterSet
from django_filters.filters import OrderingFilter
from django.db.models import Count
from ..models import Post


class CustomOrderingFilter(OrderingFilter):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.extra['choices'] += [
            ('likes', 'Likes'),
        ]

    def filter(self, qs, value):
        if value:
            if 'likes' in value:
                return qs.annotate(likes_count=Count('likes')).order_by('-likes_count')

        return super().filter(qs, value)


class PostFilterSet(FilterSet):
    order_by = CustomOrderingFilter()

    class Meta:
        model = Post
        exclude = ["id"]
        fields = {
            'id': ['exact'],
            'created_at': ['exact', 'gt', 'gte', 'lt', 'lte']
        }
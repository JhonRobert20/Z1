from django.utils.translation import gettext_lazy as _
from django.db import models


class Post(models.Model):
    
    class Visibility(models.TextChoices):
        PUBLIC = 'PB', _('Public')
        PRIVATE = 'PI', _('Private')
        PROTECTED = 'PO', _('Protected')
        
    user = models.ForeignKey(
        'users.User', related_name='posts', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    summary = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    visibility = models.CharField(choices=Visibility.choices, default=Visibility.PUBLIC, max_length=2)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']


class Like(models.Model):
    user = models.ForeignKey(
        'users.User', related_name='likes', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='likes',
                             on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('user', 'post',)

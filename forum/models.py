from django.db import models

# import User model as such to avoid circular import
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
class Discussion(models.Model):
    id = models.AutoField(primary_key=True,db_column='id')
    title = models.CharField(max_length=100,db_column='title')
    creation_date = models.DateTimeField(auto_now_add=True,db_column='creation_date')
    manager = models.ForeignKey(User, on_delete=models.CASCADE,related_name='managing_discussion',db_column='manager')
    capacity = models.IntegerField(db_column='capacity')
    joined = models.IntegerField(default=1,db_column='joined')
    class Meta:
        db_table = 'Discussion'

class UserDiscussion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,db_column='user',related_name='user_discussions')
    discussion = models.ForeignKey(Discussion, on_delete=models.CASCADE,db_column='discussion',related_name='discussion_members')
    class Meta:
        db_table = 'UserDiscussion'

from django.db import models

# import User model as such to avoid circular import
from django.contrib.auth import get_user_model
User = get_user_model()

# # Create your models here.
class Group(models.Model):
    id = models.AutoField(primary_key=True)
    group_name = models.CharField(max_length=50,db_column='group_name')
    creation_date = models.DateTimeField(auto_now_add=True,db_column='creation_date')
    manager = models.ForeignKey(User, on_delete=models.CASCADE,db_column='manager',related_name='managing_groups')
    is_qun = models.BooleanField(db_column='is_qun')
    
    class Meta:
        db_table = 'Group'

class UserGroup(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='user_groups',db_column="user")
    group = models.ForeignKey(Group, on_delete=models.CASCADE,related_name='group_members',db_column="group")
    class Meta:
        db_table = 'UserGroup'

class Messages(models.Model):
    id = models.AutoField(primary_key=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE,related_name='group_messages',db_column="group")
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='user_messages',db_column="user")
    content = models.TextField()
    SentAt = models.IntegerField()
    class Meta:
        db_table = 'Messages'

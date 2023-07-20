from django.db import models

from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(
        max_length=128,

        unique=True,
        db_column='name',
        )
    
    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Category'


# Model : Event
class Event(models.Model):
    id = models.AutoField(primary_key=True,db_column='id')
    event_name = models.CharField(max_length=128,default="",unique=True,db_column='event_name')
    host_id = models.ForeignKey(User, on_delete=models.CASCADE,null=False,default=None,related_name='hosting_events',db_column='host_id')
    category_id = models.ForeignKey(
        Category,
        # on_delete=models.CASCADE,
        default = '1',
        on_delete=models.PROTECT,
        db_column='category_id',
        related_name='events',
    )
    event_description = models.CharField(max_length=128,db_column='event_description')
    created_at = models.DateTimeField(auto_now_add=True,db_column='created_at')
    capacity = models.IntegerField(db_column='capacity')
    joined = models.IntegerField(default=1,db_column='joined')
    
    class Meta:
        db_table = 'Event'

    def __str__(self):
        return self.event_name

# Model : UserEvent (Event Member)
class UserEvent(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, db_column='user_id',related_name='user_events')
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE, db_column='event_id',related_name='event_members')
    
    class Meta:
        db_table = 'UserEvent'

    def __str__(self):
        return f"{self.user.username} - {self.event.event_name}"
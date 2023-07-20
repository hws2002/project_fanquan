from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from django.db import models
from django.utils import timezone
from .managers import CustomUserManager


class UserType(models.Model):
    id = models.AutoField(primary_key=True)

    class Meta:
        db_table = 'UserType'
        
class User(AbstractBaseUser, PermissionsMixin):
    # id = models.AutoField(primary_key=True,db_column='id') #already inherited from AbstractUser
    # password = models.CharField(max_length=50,db_column='password')#already inherited from AbstractBaseUser
    username = models.CharField(max_length=128,db_column='username',unique=True) #already inherited from AbstractUser
    email = models.EmailField(max_length=50,db_column='email',unique=True) #already inherited from AbstractUser
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default = timezone.now)
    last_login = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=128,db_column='name')
    telephone = models.IntegerField(unique=True,db_column='telephone')
    user_type = models.ForeignKey(UserType, on_delete=models.CASCADE,db_column='user_type',default = 1)
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'name', 'password','telephone','user_type']
    
    objects = CustomUserManager()
    class Meta:
        db_table = 'User'
        
    def __str__(self):
        return self.username

class Status(models.Model):
    id = models.AutoField(primary_key=True,db_column='id')
    class Meta:
        db_table = 'Status'
        
class Friendship(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_friend',db_column='user_id')
    friend_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friend_user',db_column='friend_id')
    status = models.ForeignKey(Status, on_delete=models.CASCADE, db_column='status')
    
    class Meta:
        db_table = 'Friendship'
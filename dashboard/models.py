from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from django.db import models
from django.utils import timezone
from .managers import CustomUserManager
from django.core.validators import RegexValidator

phone_regex = RegexValidator(
   regex=r'^\d{3}-\d{4}-\d{4}$',
   message="Phone number must be entered in the format: '123-4567-8901'"
)

class UserType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(
        max_length=128,
        unique=True,
        db_column='name',
        # default = 'default-user',
    )
    
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'UserType'
        
class User(AbstractBaseUser, PermissionsMixin):
    # id = models.AutoField(primary_key=True,db_column='id') #already inherited from AbstractUser
    # password = models.CharField(max_length=50,db_column='password')#already inherited from AbstractBaseUser
    username = models.CharField(max_length=128,db_column='username',unique=True,blank=False) #already inherited from AbstractUser
    email = models.EmailField(max_length=50,db_column='email',unique=True,blank=False) #already inherited from AbstractUser
    is_staff = models.BooleanField(default=False,blank=True)
    is_superuser = models.BooleanField(default=False,blank=True)
    is_active = models.BooleanField(default=True,blank=True)
    date_joined = models.DateTimeField(default = timezone.now)
    last_login = models.DateTimeField(blank=True, null=True)
    name = models.CharField(
        max_length=128,
        db_column='name',
        blank=True,
        default= "",
        null=True,
        )
    telephone = models.CharField(
        validators=[phone_regex], 
        max_length=13, 
        blank=True,
        null=True,
        )  # validators should be a list
    user_type = models.ForeignKey(
        UserType, 
        on_delete=models.CASCADE,
        db_column='user_type',
        default = 3,
        blank = False,
        )
    
    USERNAME_FIELD = 'username'
    
    REQUIRED_FIELDS = ['email','password','user_type'] # this affects prompt when creating superuser
    
    objects = CustomUserManager()
    class Meta:
        db_table = 'User'


    # Methods
    def __str__(self):
        return self.username

    def get_email_address(self):
        return self.email
    def get_telephone_number(self):
        return self.telephone

class Status(models.Model):
    id = models.AutoField(primary_key=True,db_column='id')
    name = models.CharField(
        max_length=128,
        unique=True,
        db_column='name',
        # default='pending',
        )
    
    def __str__(self):
        return self.name    
    class Meta:
        db_table = 'Status'
        
class Friendship(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_friend',db_column='user')
    friend = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friend_user',db_column='friend')
    status = models.ForeignKey(Status, on_delete=models.CASCADE, db_column='status')
    
    class Meta:
        db_table = 'Friendship'
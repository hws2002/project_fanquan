from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _

class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password,user_type,name=None,telephone=None,**extra_fields):
        if not username:
            raise ValueError('The Username field must be set')
        if not email:
            raise ValueError('The Email field must be set')
        if not user_type:
            raise ValueError('The UserType field must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email,password=password,user_type=user_type, name=name,telephone=telephone,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password,user_type, name = None, telephone=None,**extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        # Move the import statement into the method to avoid the circular import
        from .models import UserType

        # Fetch the UserType instance for superusers
        user_type_instance = UserType.objects.get(id = user_type)  # replace 'Admin' with the actual name

        # Remove user_type from extra_fields if it exists
        extra_fields.pop('user_type', None)

        return self.create_user(username, email, password, user_type_instance, name,telephone,**extra_fields)
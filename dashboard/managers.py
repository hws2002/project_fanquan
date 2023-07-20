from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _

class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where username is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, username, name,email, password,telephone,**extra_fields):
        """
        """
        if not email:
            raise ValueError(_("The email must be set"))
        if not name:
            raise ValueError(_("The name must be set"))
        if not password:
            raise ValueError(_("The password must be set"))
        if not username:
            raise ValueError(_("The username must be set"))
        if not telephone:
            raise ValueError(_("The telephone must be set"))
        
        email = self.normalize_email(email)
        user = self.model(username=username, name=name,email=email,telephone = telephone,**extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, name,email, password, telephone,**extra_fields):
        """
        """
        if not email:
            raise ValueError(_("The email must be set"))
        if not name:
            raise ValueError(_("The name must be set"))
        if not password:
            raise ValueError(_("The password must be set"))
        if not username:
            raise ValueError(_("The username must be set"))
        if not telephone:
            raise ValueError(_("The telephone must be set"))
        
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(username,name,email,password, telephone,**extra_fields)

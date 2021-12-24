"""
Managers for Custom User Model 
Dec 19, 2021
@narender

"""
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _ 


# class for Custom User Management 
class CustomUserManager(BaseUserManager):
    """
    Class for Custom User Manager.
    """
    def create_user(self, roll, email,name, password, **kwargs):
        """
        Create User with given roll number, email, password and other Arguments.
        """
        # if roll no not given
        if not roll:
            raise ValueError(_("Roll Number Field should not be empty"))
        
        email = self.normalize_email(email) 
        user = self.model(
            roll = roll ,
            email = email,
            name=name,
            **kwargs 
        )

        user.set_password(password)
        user.save()

        return user 

    def create_superuser(self, roll, email,name, password, **kwargs):
        """
        Create Superuser with given roll number, email, password and other arguments.
        """
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)
        kwargs.setdefault('is_active', True)

        if kwargs.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if kwargs.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))

        return self.create_user(roll,email,name,password,**kwargs)
        
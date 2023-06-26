from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.conf import settings

class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""
    def create_user(self, email, name, password=None):
        """create a new user profile"""
        if not email: 
            raise ValueError("must have email address")
        
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self, email, name, password):
        """create and save a new superuser with given details"""
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database Modal for users in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_fullname(self): 
        """fullname for user"""
        return self.name 
    
    def get_shortname(self):
        """shortname of user"""
        return self.name
    
    def __str__(self): 
        """return object of this class the way i want"""
        return f"email: {self.email} \n name: {self.name} \n is_active: {self.is_active} \n is_staff: {self.is_staff}"
    


class ProfileFeedItem(models.Model): 
    """Profile status update"""
    user_profile = models.ForeignKey(
        settings.AUTH_USER_MODEL,  
        on_delete=models.CASCADE     
    )

    status_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)


    def __str__(self): 
        """Return the model as string"""
        return self.status_text

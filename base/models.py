from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .managers import CustomManager, Gender, Room, Block, Sharing
# Create your models here.



class CustomUser(AbstractBaseUser):
    name = models.CharField(max_length=50,default=False)
    email = models.EmailField('email_address', unique=True)
    USN = models.CharField(max_length=10, default=False)
    course = models.CharField(max_length=50, default=False)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE, null=True)
    room_no = models.ForeignKey(Room, on_delete=models.CASCADE, null=True, default = False)
    block_name = models.ForeignKey(Block, on_delete=models.CASCADE, null=True, default = False)
    sharing = models.ForeignKey(Sharing, on_delete=models.CASCADE, null=True, default = False)
    mother_name = models.CharField(max_length=50, default=False)
    father_name = models.CharField(max_length=50, default=False)
    contact = models.CharField(max_length=10, default=False)
    mother_contact = models.CharField(max_length=10, default=False)
    father_contact = models.CharField(max_length=10, default=False)
    
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    # updated = models.DateTimeField(auto_now=True)
    # created = models.DateTimeField(auto_now_add=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomManager()
    

    def has_perm(self, perm, obj=None):
        return self.is_superuser
    
    def has_module_perms(self, app_label):
        return self.is_superuser

    def __str__(self):
        return self.email
    

from django.db import models
#from django.contrib.auth.models import AbstractUser
#from django.contrib.auth  import get_user_model
from ckeditor.fields import RichTextField
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
# Create your models here.


class CustomUser(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    is_active = models.BooleanField(default=False)
#from ckeditor_uploader.fields import
#from ckeditor.widgets import CKEditorWidget
# Create your models here.

#User= get_user_model()

#class MyUser(AbstractUser): pass


class NavbarModel(models.Model):
    title=models.CharField(max_length=100, null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    def __str__(self):
        return f'{self.title}'

class NavbarGuestModel(models.Model):
    title=models.CharField(max_length=100, null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    def __str__(self):
        return f'{self.title}'

class Settings(models.Model):
    background_image = models.ImageField(upload_to='blog_images',null=True,blank=True)
    blog_title = models.CharField(max_length=50,null=True,blank=True)
    blog_subtitle_f = models.CharField(max_length=100,null=True,blank=True)
    blog_subtitle_s = models.CharField(max_length=100,null=True,blank=True)
    blog_subtitle_t = models.CharField(max_length=100,null=True,blank=True)
    logo = models.ImageField(upload_to='blog_logo',null=True,blank=True)

class Footer(models.Model):
    title= models.CharField(max_length=100, null=True, blank=True)
    text=models.CharField(max_length=100, null=True, blank=True)
    url= models.URLField(null=True, blank=True)


class WorksSectionModel(models.Model):
    title=models.CharField(max_length=100,null=True,blank=True)
    subtitle=models.CharField(max_length=500,null=True,blank=True)

class WorkModel(models.Model):
    user_id=models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    work_title=models.CharField(max_length=100,null=True,blank=True)
    work_subtitle=models.CharField(max_length=100,null=True,blank=True)
    work_date=models.DateField(auto_now=True)
    work_text=RichTextField(null=True,blank=True)
    work_head_image=models.ImageField(upload_to='work_image',null=True, blank=True)
    work_foot_image=models.ImageField(upload_to='work_image',null=True, blank=True)
    is_activated=models.BooleanField(default=False)
    def __str__(self):
        return f'{self.work_title}/{self.work_subtitle}'

class WorkImageModel(models.Model):
    work_id=models.ForeignKey('WorkModel',on_delete=models.CASCADE)
    #description=models.CharField(max_length=100,null=True,blank=True)
    images=models.ImageField(upload_to='work_image',null=True, blank=True)

class AboutModel(models.Model):
    about_subtitle=models.CharField(max_length=100,null=True,blank=True)
    about_text = models.TextField(null=True, blank=True)

class AboutImageModel(models.Model):
    about_title=models.CharField(max_length=100,null=True,blank=True)
    images=models.ImageField(upload_to='about_image',null=True, blank=True)

class ContactModel(models.Model):
    email=models.EmailField()
    subject=models.CharField(max_length=100, null=True, blank=True)
    message =models.TextField()

class ContactAddressModel(models.Model):
    phone_number=models.CharField(max_length=20,null=True, blank=True)
    email=models.EmailField()
    address=models.CharField(max_length=100,null=True, blank=True)

class ContactSocNetModel(models.Model):
    url=models.URLField(null=True, blank=True)
    icon=models.ImageField(upload_to='contact_image',null=True, blank=True)

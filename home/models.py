from __future__ import absolute_import
from django.db import models
from django.core.urlresolvers import reverse
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import BaseUserManager, \
                                         AbstractBaseUser, \
                                         PermissionsMixin
from phonenumber_field.modelfields import PhoneNumberField


class Product(models.Model):
    title = models.CharField('TITLE', max_length=50, help_text="상품명")
    content = RichTextUploadingField()
    price = models.IntegerField(blank=False, default= 0, help_text="가격")
    create_date =models.DateTimeField('Create Date', auto_now_add = True)
    modify_date = models.DateTimeField('Modify Date', auto_now = True)
    discount_percent = models.IntegerField(help_text="할인률")
    rating = models.IntegerField(default= 0, help_text="평점")

    choice = (
        ('Discount', 'Discount'),
        ('Sale', 'Sale'),
        ('TimeSale', 'TimeSale'),
        ('Normal', 'Normal')
    )
    choice_field = models.CharField(max_length= 10, choices=choice)

    """ 
       size = (
            ('S', 'Small'),
            ('M', 'Medium'),
            ('L', 'Large'),
            ('XL', 'XLarge')
        )

       size_field = models.CharField(max_length=3, choices=size)

       color = (
            ('Red', 'Red'),
            ('Blue', 'Blue'),
            ('White', 'White'),
            ('Black', 'Black')
        )

       color_field = models.CharField(max_length=3, choices=color)
    """

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'
        db_table = 'all_products'
        ordering = ('-create_date',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('single_product', args=(self.id,))

    def get_previous_post(self):
        return self.get_previous_by_modify_date()

    def get_next_post(self):
        return self.get_next_by_modify_date()

def get_upload_path(instance, filename):
    return "media/%s" % (filename)

class Photo(models.Model):
    product = models.ForeignKey(Product, null=True)
    image = models.ImageField(upload_to= get_upload_path,
                              verbose_name='Image', )

class Size(models.Model):
    product = models.ForeignKey(Product, null=True)
    S_size = models.IntegerField()


class MyUserManager(BaseUserManager):
    def create_user(self, email, date_of_birth,
                    name, address, phone_number, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, date_of_birth, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            date_of_birth=date_of_birth,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class CustomUser(AbstractBaseUser,  PermissionsMixin) :
    email = models.EmailField(verbose_name='email', max_length=128, blank=False, unique =True)
    name = models.CharField(verbose_name='name', max_length=256, blank=True)
    date_of_birth = models.DateTimeField()
    phone_number = PhoneNumberField()
    address = models.CharField(max_length=150, null=False, blank=True, help_text="주소를 입력하세요")

    USERNAME_FIELD = 'email'
    EMAIL_FIELD ='email'
    REQUIRED_FIELDS = [
        'email',
        'phone_number',
        'birthday',
        'address',
    ]

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)


    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


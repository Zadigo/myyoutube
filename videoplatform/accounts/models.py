
from accounts import managers
from accounts.utils import avatar_path
from accounts.validators import avatar_extension_validator
from django.apps.registry import apps
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.db.models.constraints import UniqueConstraint
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from django.utils.crypto import get_random_string
from django.utils.timezone import now, timedelta
from django.utils.translation import gettext_lazy as _
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """Base user model"""

    username_validator = UnicodeUsernameValidator()

    email = models.EmailField(
        max_length=255,
        unique=True
    )
    username = models.CharField(
        verbose_name=_("username"),
        max_length=150,
        help_text=_(
            "Required. 150 characters or fewer. "
            "Letters, digits and @/./+/-/_ only."
        ),
        validators=[username_validator],
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )
    firstname = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )
    lastname = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )
    is_active = models.BooleanField(
        default=False,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        )
    )
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = managers.CustomUserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return f'My User: {self.email}'

    class Meta:
        verbose_name = _('myuser')
        verbose_name_plural = _('myusers')
        indexes = [
            models.Index(
                fields=['is_active'],
                name='active_accounts',
                condition=models.Q(is_active=True)
            )
        ]

    @property
    def get_full_name(self):
        return f'{self.firstname} {self.lastname}'

    @property
    def get_short_name(self):
        return self.firstname

    @property
    def get_short_name(self):
        return self.firstname

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)


class UserProfile(models.Model):
    """User profile model"""
    myuser = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE
    )
    avatar = models.ImageField(
        upload_to=avatar_path,
        validators=[avatar_extension_validator],
        blank=True,
        null=True
    )
    avatar_thumbnail = ImageSpecField(
        processors=ResizeToFill(width=100, height=100),
        format='JPEG',
        options={'quality': 50}
    )
    customer_id = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text='Stripe customer ID'
    )
    birthdate = models.DateField(
        default=timezone.now,
        blank=True,
        null=True
    )
    telephone = models.CharField(
        max_length=20,
        blank=True,
        null=True
    )
    address = models.CharField(
        max_length=150,
        blank=True,
        null=True
    )
    city = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )
    zip_code = models.IntegerField(
        blank=True,
        null=True
    )
    is_professional = models.BooleanField(
        default=False
    )
    created_on = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f'My User Profile: {self.myuser.email}'

    @property
    def get_full_address(self):
        return f'{self.address}, {self.city}, {self.zip_code}'


class ActivationToken(models.Model):
    myuser = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE
    )
    token = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )
    expiration_date = models.DateTimeField(blank=True, null=True)
    creation_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.token or 'tok-'

    class Meta:
        constraints = [
            UniqueConstraint(
                fields=['token', 'myuser'],
                name='one_token_per_user'
            )
        ]

    @property
    def is_valid(self):
        return now() <= self.expiration_date

    def clean(self):
        if self.expiration_date is None:
            d = now() + timedelta(days=1)
            self.expiration_date = d

        if self.token is None:
            self.token = get_random_string(length=30)


@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(myuser=instance)
        model = apps.get_model('videos.ViewingProfile')
        profile, state = model.objects.get_or_create(user=instance)


# @receiver(post_save, sender=CustomUser)
# def create_activation_token(sender, instance, created, **kwargs):
#     if created:
#         ActivationToken.objects.create(
#             myuser=instance,
#             token=get_random_string(length=30)
#         )

# @receiver(post_delete, sender=UserProfile)
# def delete_old_avatar(sender, instance, **kwargs):
#     is_s3_backend = False
#     try:
#         is_s3_backend = settings.USE_S3
#     except:
#         pass

#     if not is_s3_backend:
#         if instance.avatar.url:
#             if os.path.isfile(instance.avatar.path):
#                 os.remove(os.avatar.path)
#     else:
#         instance.url.delete(save=False)


# @receiver(pre_save, sender=UserProfile)
# def delete_avatar_on_update(sender, instance, **kwargs):
#     is_s3_backend = False
#     try:
#         is_s3_backend = settings.USE_S3
#     except:
#         pass

#     if not is_s3_backend:
#         if instance.pk:
#             try:
#                 old_image = UserProfile.objects.get(pk=instance.pk)
#             except:
#                 return False
#             else:
#                 new_image = instance.url
#                 if old_image and old_image != new_image:
#                     if os.path.isfile(old_image.url.path):
#                         os.remove(old_image.url.path)
#     else:
#         instance.url.delete(save=False)


# @receiver(pre_save, sender=UserProfile)
# def delete_old_avatar(sender, instance, **kwargs):
#     if instance.pk:
#         try:
#             old_avatar = UserProfile.objects.get(pk=instance.pk)
#         except:
#             return False
#         else:
#             new_avatar = instance.avatar
#             if old_avatar and old_avatar != new_avatar:
#                 if os.path.isfile(old_avatar.avatar.path):
#                     os.remove(old_avatar.avatar.path)

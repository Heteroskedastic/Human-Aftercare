import os

from django.contrib.auth import get_user_model
from django.db import models, connections
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_tenants.utils import get_tenant_database_alias, get_public_schema_name
from phonenumber_field.modelfields import PhoneNumberField


User = get_user_model()

def avatar_file_path_func(instance, filename):
    from human_aftercare.helpers.utils import get_random_upload_path
    return get_random_upload_path(os.path.join('uploads', 'profile_avatar'), filename)


class UserProfile(models.Model):
    GENDER_UNKNOWN = 'o'
    GENDER_MALE = 'm'
    GENDER_FEMALE = 'f'
    GENDER_CHOICES = (
        (GENDER_UNKNOWN, 'Other'),
        (GENDER_MALE, 'Male'),
        (GENDER_FEMALE, 'Female'),
    )

    user = models.OneToOneField(User, primary_key=True, related_name='profile', on_delete=models.CASCADE)
    birth_date = models.DateField('Date of birth', blank=True, null=True)
    gender = models.CharField('Gender', max_length=1, choices=GENDER_CHOICES, default=GENDER_UNKNOWN)
    avatar = models.ImageField('Avatar', blank=True, null=True, upload_to=avatar_file_path_func)

    def __str__(self):
        return '{}'.format(self.user)


class Resident(models.Model):
    GENDER_MALE = 'm'
    GENDER_FEMALE = 'f'
    GENDER_OTHER = 'o'
    GENDER_CHOICES = (
        (GENDER_MALE, 'Male'),
        (GENDER_FEMALE, 'Female'),
        (GENDER_OTHER, 'Other'),
    )

    EYE_COLOR_BLACK = 'BLK'
    EYE_COLOR_BLUE = 'BLU'
    EYE_COLOR_BROWN = 'BRO'
    EYE_COLOR_GRAY = 'GRY'
    EYE_COLOR_GREEN = 'GRN'
    EYE_COLOR_HAZEL = 'HAZ'
    EYE_COLOR_MAROON = 'MAR'
    EYE_COLOR_MULTICOLORED = 'MUL'
    EYE_COLOR_PINK = 'PNK'
    EYE_COLOR_UNKNOWN = 'XXX'
    EYE_COLOR_OPTIONS = (
        (EYE_COLOR_BLACK, 'Black'),
        (EYE_COLOR_BLUE, 'Blue'),
        (EYE_COLOR_BROWN, 'Brown'),
        (EYE_COLOR_GRAY, 'Gray'),
        (EYE_COLOR_GREEN, 'Green'),
        (EYE_COLOR_HAZEL, 'Hazel'),
        (EYE_COLOR_MAROON, 'Maroon'),
        (EYE_COLOR_MULTICOLORED, 'Multi-Colored'),
        (EYE_COLOR_PINK, 'PNK'),
        (EYE_COLOR_UNKNOWN, 'Unknown'),
    )

    HAIR_COLOR_BALD = 'BAL'
    HAIR_COLOR_BLACK = 'BLK'
    HAIR_COLOR_BLONDE = 'BLN'
    HAIR_COLOR_BROWN = 'BRO'
    HAIR_COLOR_GRAY = 'GRY'
    HAIR_COLOR_GREEN = 'GRN'
    HAIR_COLOR_ORANGE = 'ONG'
    HAIR_COLOR_PURPLE = 'PLE'
    HAIR_COLOR_PINK = 'PNK'
    HAIR_COLOR_RED = 'RED'
    HAIR_COLOR_SANDY = 'SDY'
    HAIR_COLOR_WHITE = 'WHI'
    HAIR_COLOR_UNKNOWN = 'XXX'
    HAIR_COLOR_OPTIONS = (
        (HAIR_COLOR_BALD, 'Bald'),
        (HAIR_COLOR_BLACK, 'Black'),
        (HAIR_COLOR_BLONDE, 'Blonde or strawberry'),
        (HAIR_COLOR_BROWN, 'Brown'),
        (HAIR_COLOR_GRAY, 'Gray or partially gray'),
        (HAIR_COLOR_GREEN, 'Green'),
        (HAIR_COLOR_ORANGE, 'Orange'),
        (HAIR_COLOR_PURPLE, 'Purple'),
        (HAIR_COLOR_PINK, 'Pink'),
        (HAIR_COLOR_RED, 'Red or auburn'),
        (HAIR_COLOR_SANDY, 'Sandy'),
        (HAIR_COLOR_WHITE, 'White'),
        (HAIR_COLOR_UNKNOWN, 'Unknown'),
    )

    first_name = models.CharField('First Name', max_length=100)
    middle_name = models.CharField('Middle Name', max_length=100, blank=True, null=True)
    last_name = models.CharField('Last Name', max_length=100)
    birth_date = models.DateField('Birth Date')
    gender = models.CharField('Gender', max_length=1, choices=GENDER_CHOICES)
    eye_color = models.CharField('Eye Color', max_length=24, choices=EYE_COLOR_OPTIONS, default=EYE_COLOR_UNKNOWN)
    hair_color = models.CharField('Hair Color', max_length=24, choices=HAIR_COLOR_OPTIONS, default=HAIR_COLOR_UNKNOWN)
    phone_number = PhoneNumberField(null=True, blank=True, unique=True)
    email = models.EmailField(null=True, blank=True, unique=True)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, **kwargs):
    if kwargs.get('created'):
        connection = connections[get_tenant_database_alias()]
        schema_name = getattr(connection, 'schema_name', None)
        public_schema = get_public_schema_name()
        if public_schema != schema_name:
            UserProfile.objects.create(user=instance)

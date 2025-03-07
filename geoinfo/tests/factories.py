"""Provides factories for student models."""
import factory  # pylint: disable=import-error

from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser

PASSWORD = 'password'


class UserFactory(factory.django.DjangoModelFactory):
    """ User factory. """
    username = email = factory.Sequence(lambda n: f'user{n}')
    email = factory.Sequence(lambda n: f'user{n}@example.com')
    password = factory.PostGenerationMethodCall('set_password', PASSWORD)
    is_active = True
    is_superuser = False
    is_staff = False

    class Meta:
        model = get_user_model()


class AnonymousUserFactory(factory.Factory):
    class Meta:
        model = AnonymousUser

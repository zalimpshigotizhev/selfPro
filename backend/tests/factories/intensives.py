import factory
from factory.django import DjangoModelFactory

from core.apps.intensives.models.intensives import Intensive


class IntensiveModelFactory(DjangoModelFactory):
    title = factory.Faker("first_name")
    color = factory.Faker("color")

    class Meta:
        model = Intensive

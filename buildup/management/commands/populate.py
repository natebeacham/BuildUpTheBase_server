import os
import faker
import random

from django.core.files import File
from django.core.management.base import BaseCommand, CommandError

from buildup.models import Player

fake = faker.Faker()

class Command(BaseCommand):
	help = 'Populates db with crap data'

	def handle(self, *args, **options):
		for x in range(100):
			Player.objects.create(
				username=fake.user_name(),
				coins=random.randint(1, 1000000000),
			)
from django.db import models
from django.contrib.gis.db.models import PointField
from django.contrib.auth import get_user_model

User = get_user_model()


class Gym(models.Model):

	location = PointField(blank=False)
	name = models.CharField(max_length = 100, blank=False)
	contact_no = models.IntegerField(blank=False)
	rating = models.IntegerField(default=0)
	rated_by = models.ManyToManyField(User)

	def __str__(self):
		return self.name
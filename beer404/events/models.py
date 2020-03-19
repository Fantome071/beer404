from django.db import models

from django.contrib.auth.models import User


class Event(models.Model):
  """
  Event Model for Event Management
  """

  id = models.AutoField(primary_key=True)
  creator = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='creator', null=True)
  name = models.CharField(max_length=150, null=False)
  description = models.CharField(max_length=255)
  nb_place = models.IntegerField()
  date_event = models.DateField()
  time_event = models.TimeField()
  address = models.CharField(max_length=255)
  coord_x = models.FloatField()
  coord_y = models.FloatField()
  participate = models.ManyToManyField(User)

  def __str__(self):
    return "{0} : Event = {1} | Creator = {2} | Description = {3}".format(
      self.id,
      self.creator,
      self.description
    )

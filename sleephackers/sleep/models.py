from django.db import models

# Create your models here.

class Workouts(models.Model):
    date = models.IntegerField()
    time_completed = models.BigIntegerField()
    distance = models.BigIntegerField()
    calories = models.FloatField()
    wo_count = models.IntegerField()
    bmr = models.FloatField()
    km = models.FloatField()
    wo_time = models.IntegerField()
    steps = models.IntegerField()
    active_time = models.BigIntegerField()

    def __unicode__(self):
        return self.date

class Meals(models.Model):
    date = models.IntegerField()
    fiber = models.FloatField()
    polyunsaturated_fat = models.FloatField()

class Sleep(models.Model):
    date = models.IntegerField()
    awakenings = models.IntegerField()
    asleep_time = models.BigIntegerField()
    awake_time = models.BigIntegerField()


class DayFacts(models.Model):
    date = models.IntegerField()
    feature = models.CharField()
    value = models.CharField()

    def __unicode__(self):
        return self.date

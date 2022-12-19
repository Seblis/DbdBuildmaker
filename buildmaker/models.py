from django.db import models

# Create your models here.


class Perk(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=500)
    image_name = models.CharField(max_length=50)

    class Meta:
        abstract = True


class KillerPerk(Perk):
    pass


class SurvivorPerk(Perk):
    pass


class Build(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        abstract = True


class KillerBuild(Build):
    pass


class SurvivorBuild(Build):
    pass

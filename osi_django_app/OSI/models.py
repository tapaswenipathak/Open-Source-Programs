from django.db import models
from django.shortcuts import reverse

class soc(models.Model):
    title = models.CharField(max_length=50)
    soc_homepage = models.URLField(default=None)
    stipend = models.BooleanField(default=False)
    timeline = models.URLField(blank=True)
    publish = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('soc')

class osc(models.Model):
    title = models.CharField(max_length=50)
    osc_homepage = models.URLField(default=None)
    awards = models.CharField(max_length=50)
    timeline = models.URLField(blank=True)
    publish = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('osc')

class univ_soc_woc(models.Model):
    title = models.CharField(max_length=50)
    homepage = models.URLField(default=None)
    awards = models.CharField(max_length=50)
    timeline = models.URLField(blank=True)
    publish = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('u-soc-woc')

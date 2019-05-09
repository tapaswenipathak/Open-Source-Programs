from django.db import models

class soc(models.Model):
    title = models.CharField(max_length=50)
    soc_homepage = models.URLField(default=None)
    stripend = models.BooleanField(default=False)
    timeline = models.URLField(default=None)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('soc')

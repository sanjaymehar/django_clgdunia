from django.db import models
from django.utils.translation import gettext as _
from django.urls import reverse
# Create your models here.
class Carsale(models.Model):
    Manufacturer=models.CharField(_("Manufacturer"),max_length=255)
    Model=models.CharField(_("Model"),max_length=255)
    Sales_in_thousands=models.DecimalField(_("Sales_in_thousands"),max_digits=7,decimal_places=3)
    Price_in_thousands=models.DecimalField(_("Price_in_thousands"),max_digits=7,decimal_places=3)
    Engine_size=models.DecimalField(_("Engine_size"),max_digits=7,decimal_places=3)
    Horsepower=models.IntegerField(_("Horsepower"))
    Fuel_capacity=models.DecimalField(_("Fuel_capacity"),max_digits=7,decimal_places=3)
    Fuel_efficiency=models.IntegerField(_("Fuel_efficiency"))

    def __str__(self):
        return self.Model

    def get_absolute_url(self):
            return reverse('clgdunia:home')
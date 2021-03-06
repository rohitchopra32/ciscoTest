from django.core.validators import validate_ipv4_address
from django.db import models
from router.validators import validate_mac_address


# Create your models here.


class Router(models.Model):
    """
    This is router models that holds the unique router properties i.e Sapid, Host Name, Loopback, Mac Address.
    """
    ROUTER_CHOICES = (
        ('0', 'Select Router Type'),
        ('AG1', 'AG1'),
        ('CSS', 'CSS')
    )
    router_type = models.CharField(max_length=3, choices=ROUTER_CHOICES, default='0')
    sap_id = models.CharField(max_length=18)
    host_name = models.CharField(max_length=14, unique=True)
    loopback = models.CharField(max_length=15, unique=True, validators=[validate_ipv4_address])
    mac_address = models.CharField(max_length=17, validators=[validate_mac_address])
    is_active = models.BooleanField(default=True, help_text="For Soft Delete")

    class Meta:
        ordering = ("-id",)

    def __str__(self):
        return self.router_type

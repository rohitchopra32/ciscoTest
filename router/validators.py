import re

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_mac_address(value):
    if not re.match("[0-9a-f]{2}([-:]?)[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$", value.lower()):
        raise ValidationError(
            'Mac Address is invalid: {}'.format(value),
        )
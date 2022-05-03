# yourapp.validators.py

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_domainonly_email(value):
    """
    Let's validate the email passed is in the domain "yourdomain.com"
    """
    if not "yourdomain.com" in value:
        raise ValidationError(_("Sorry, the email submitted is invalid. All emails have to be registered on this domain only."))
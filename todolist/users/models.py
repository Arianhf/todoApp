from django.db import models

from django.contrib.auth.models import AbstractUser
from django.db import models


# added for extendability
class CustomUser(AbstractUser):
    pass

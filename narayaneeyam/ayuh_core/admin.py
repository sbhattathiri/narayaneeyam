from django.contrib import (
    admin,
)
from django.contrib.auth.admin import (
    UserAdmin,
)

from ayuh_core import (
    models,
)

admin.site.register(models.AyuhUser, UserAdmin)

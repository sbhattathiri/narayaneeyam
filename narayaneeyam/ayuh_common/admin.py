from ayuh_common import (
    models,
)

from django.contrib import (
    admin,
)
from django.contrib.auth.admin import (
    UserAdmin,
)

admin.site.register(models.AyuhUser, UserAdmin)

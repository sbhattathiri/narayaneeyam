from ayuh import (
    settings,
)

from django.db import (
    models,
)


class TimestampedModelMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class UserStampedModelMixin(models.Model):
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="%(class)s_updated_by",
        help_text="The user who last updated this record.",
    )

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        from django.contrib.auth.models import (
            AnonymousUser,
        )

        current_user = getattr(self, "_current_user", None)
        if current_user and not isinstance(current_user, AnonymousUser):
            self.updated_by = current_user

        super().save(*args, **kwargs)

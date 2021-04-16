from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _
from django.db.models import signals


class CommentConfig(AppConfig):
    name = 'com'
    verbose_name = _('com')

    def ready(self):
        import com.signals

        signals.post_migrate.connect(com.signals.create_permission_groups, sender=self)
        signals.post_migrate.connect(com.signals.adjust_flagged_comments, sender=self)

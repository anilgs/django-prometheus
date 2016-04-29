from django_prometheus.db.common import DatabaseWrapperMixin
from django.db.backends.postgresql_psycopg2 import base
from django.db.backends import utils


class DatabaseFeatures(base.DatabaseFeatures):
    """Our database has the exact same features as the base one."""
    pass


class DatabaseWrapper(DatabaseWrapperMixin, base.DatabaseWrapper):
    CURSOR_CLASS = utils.CursorWrapper

from ormar import ModelMeta

from huda_fastapi.db.config import database
from huda_fastapi.db.meta import meta


class BaseMeta(ModelMeta):
    """Base metadata for models."""

    database = database
    metadata = meta

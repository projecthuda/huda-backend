from databases import Database

from huda_fastapi.settings import settings

database = Database(str(settings.db_url))

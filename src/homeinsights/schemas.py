from datetime import datetime

from pydantic import BaseModel


class HAState(BaseModel):
    entity_id: str
    state: float
    last_changed: datetime

from datetime import datetime
from typing import Annotated

from pydantic import BaseModel, BeforeValidator

# HA reports these when a sensor is offline or hasn't reported yet
_NO_READING = {"unavailable", "unknown"}


def _none_if_no_reading(value: object) -> object:
    return None if value in _NO_READING else value


class HAState(BaseModel):
    entity_id: str
    state: Annotated[float | None, BeforeValidator(_none_if_no_reading)]
    last_changed: datetime

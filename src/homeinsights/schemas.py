import math
from datetime import datetime

from pydantic import BaseModel


class HAState(BaseModel):
    entity_id: str
    state: str  # HA sends every state as a string
    last_changed: datetime

    @property
    def value(self) -> float | None:
        """Numeric reading, or None for 'unavailable', 'unknown', etc."""
        try:
            v = float(self.state)
        except ValueError:
            return None
        return v if math.isfinite(v) else None

from datetime import datetime, timezone

from homeinsights.mappers import to_reading_row
from homeinsights.models import Reading
from homeinsights.schemas import HAState


def test_mapper_populates_every_column():
    state = HAState(entity_id="sensor.x", state="21.5", last_changed=datetime.now(timezone.utc))
    row = to_reading_row(state)
    columns = {c.name for c in Reading.__table__.columns} - {"id"}
    assert set(row) == columns

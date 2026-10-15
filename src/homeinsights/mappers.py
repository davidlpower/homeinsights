from homeinsights.schemas import HAState


def to_reading_row(state: HAState) -> dict:
    """Map an HA payload object to the column names of the readings table."""
    return {
        "entity_id": state.entity_id,
        "value": state.state,
        "recorded_at": state.last_changed,
    }

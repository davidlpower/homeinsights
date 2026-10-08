from datetime import datetime

import httpx
from pydantic import TypeAdapter

from homeinsights.schemas import HAState
from homeinsights.settings import settings

# History comes back as a list of lists: one inner list per entity
_history = TypeAdapter(list[list[HAState]])


def make_client() -> httpx.AsyncClient:
    return httpx.AsyncClient(
        base_url=settings.ha_base_url,
        headers={"Authorization": f"Bearer {settings.ha_token.get_secret_value()}"},
        timeout=30.0,
    )


async def fetch_history(client: httpx.AsyncClient, entity_id: str, start: datetime, end: datetime) -> list[HAState]:
    response = await client.get(
        f"/api/history/period/{start.isoformat()}",
        params={"filter_entity_id": entity_id, "end_time": end.isoformat()},
    )
    response.raise_for_status()
    return [state for series in _history.validate_python(response.json()) for state in series]

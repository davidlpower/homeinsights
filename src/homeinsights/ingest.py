import asyncio
from datetime import datetime, timedelta, timezone

from sqlalchemy.dialects.postgresql import insert

from homeinsights.db import SessionLocal
from homeinsights.ha_client import fetch_history, make_client
from homeinsights.mappers import to_reading_row
from homeinsights.models import Reading
from homeinsights.schemas import HAState

ENTITIES = ["sensor.living_room_temperature"]


async def store(states: list[HAState]) -> None:
    if not states:
        return
    rows = [to_reading_row(s) for s in states]
    stmt = insert(Reading).values(rows).on_conflict_do_nothing(index_elements=["entity_id", "recorded_at"])
    async with SessionLocal() as session:
        await session.execute(stmt)
        await session.commit()


async def main() -> None:
    end = datetime.now(timezone.utc)
    start = end - timedelta(days=1)

    async with make_client() as client:
        for entity_id in ENTITIES:
            states = await fetch_history(client, entity_id, start, end)
            await store(states)
            print(f"{entity_id}: fetched {len(states)} states")


def run() -> None:
    """Synchronous entry point used by the `home-insights-ingest` script."""
    asyncio.run(main())


if __name__ == "__main__":
    run()

"""Local security-event primitives.

Media persistence and retention will be implemented here without any cloud
upload. Events are intentionally represented separately from recognition so
the policy can be changed without rewriting the AI layer.
"""

from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path


@dataclass
class SecurityEvent:
    event_type: str
    label: str
    created_at: str


def create_event(event_type: str, label: str) -> SecurityEvent:
    return SecurityEvent(
        event_type=event_type,
        label=label,
        created_at=datetime.now(timezone.utc).isoformat(),
    )


def ensure_storage(root: str | Path) -> Path:
    path = Path(root)
    path.mkdir(parents=True, exist_ok=True)
    for name in ("snapshots", "recordings", "audio", "faces"):
        (path / name).mkdir(exist_ok=True)
    return path

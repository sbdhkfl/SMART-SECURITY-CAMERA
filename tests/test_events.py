from orange_pi.app.events import create_event, ensure_storage


def test_create_event():
    event = create_event("unknown_face", "unknown")
    assert event.event_type == "unknown_face"
    assert event.label == "unknown"
    assert event.created_at


def test_ensure_storage(tmp_path):
    root = ensure_storage(tmp_path / "camera")
    assert (root / "snapshots").is_dir()
    assert (root / "recordings").is_dir()
    assert (root / "audio").is_dir()
    assert (root / "faces").is_dir()

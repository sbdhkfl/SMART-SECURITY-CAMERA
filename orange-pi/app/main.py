"""Initial local camera service.

This first implementation deliberately focuses on safe local plumbing:
configuration, health endpoint, and a camera-stream status check.
Face recognition and event capture are added as separate modules so each
piece can be tested independently.
"""

from pathlib import Path
import time
import cv2
import yaml
from fastapi import FastAPI

ROOT = Path(__file__).resolve().parents[2]
CONFIG_PATH = ROOT / "config" / "config.yaml"

app = FastAPI(title="SMART-SECURITY-CAMERA", version="0.1.0")


def load_config() -> dict:
    if not CONFIG_PATH.exists():
        return {}
    with CONFIG_PATH.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle) or {}


@app.get("/health")
def health() -> dict:
    return {
        "ok": True,
        "service": "smart-security-camera",
        "timestamp": time.time(),
        "config_loaded": CONFIG_PATH.exists(),
    }


@app.get("/camera/check")
def camera_check() -> dict:
    config = load_config()
    url = config.get("camera", {}).get("stream_url")
    if not url:
        return {"ok": False, "error": "camera.stream_url is not configured"}

    cap = cv2.VideoCapture(url)
    opened = cap.isOpened()
    cap.release()
    return {"ok": opened, "stream_configured": True}

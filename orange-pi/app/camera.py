"""Camera stream utilities."""

from dataclasses import dataclass
import cv2


@dataclass
class CameraFrame:
    ok: bool
    frame: object | None = None


class CameraClient:
    def __init__(self, stream_url: str):
        self.stream_url = stream_url
        self.capture = None

    def open(self) -> bool:
        self.capture = cv2.VideoCapture(self.stream_url)
        return bool(self.capture.isOpened())

    def read(self) -> CameraFrame:
        if self.capture is None and not self.open():
            return CameraFrame(False)
        ok, frame = self.capture.read()
        return CameraFrame(bool(ok), frame if ok else None)

    def close(self) -> None:
        if self.capture is not None:
            self.capture.release()
            self.capture = None

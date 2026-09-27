# 03 - Hardware and Wiring

## Main parts

| Part | Job |
|---|---|
| Orange Pi Zero 3 | Local AI, storage, audio, API, dashboard |
| ESP32-S3-CAM | Camera capture and network stream |
| USB microphone | Unknown-person response recording |
| microSD/storage | OS, models, database, photos, video, audio |
| Network | Local communication; Internet only for optional remote access |

## Important

ESP32-S3-CAM boards are sold with different camera sensors and pin mappings. Do not blindly use a pinout from another board.

Before wiring the camera, identify the exact ESP32-S3-CAM board and camera sensor. The firmware directory will contain a board-specific pin configuration.

## Orange Pi connections

- USB microphone -> Orange Pi USB port.
- ESP32-S3-CAM -> network; no serial connection is required for normal camera streaming.
- Orange Pi -> power according to the board manufacturer's specification.

The camera stream is network-based, so the ESP32 and Orange Pi need to be reachable on the same LAN during initial setup.

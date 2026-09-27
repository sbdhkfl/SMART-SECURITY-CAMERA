# ESP32-S3-CAM Firmware

This directory will contain the camera firmware.

The exact camera pin mapping is intentionally not hard-coded yet because ESP32-S3-CAM boards use different layouts and sensors.

## Planned firmware behavior
- connect to configured Wi-Fi
- start the camera
- expose a local MJPEG stream
- expose a health endpoint
- reconnect after Wi-Fi loss
- avoid cloud services
- keep credentials in a local configuration file that is excluded from Git

## Required before flashing

Identify the exact ESP32-S3-CAM board model and camera sensor. Once identified, the matching pins can be added to a board-specific configuration without risking incorrect wiring.

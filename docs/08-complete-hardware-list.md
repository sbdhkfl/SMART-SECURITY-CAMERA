# 08 - Complete Hardware List

## Required core hardware

| Item | Quantity | Purpose |
|---|---:|---|
| Orange Pi Zero 3 2GB | 1 | Main computer, AI, storage, API |
| 64GB or larger microSD | 1 | OS and application storage |
| ESP32-S3-CAM | 1 | Camera |
| Compatible camera sensor/lens | 1 | Image capture; normally supplied with the board |
| USB microphone | 1 | Voice-response recording |
| USB-C power supply for Orange Pi | 1 | Stable Orange Pi power |
| USB cable/power supply for ESP32-S3-CAM | 1 | Camera power/programming |
| Wi-Fi/LAN router | 1 | Local network; Internet is optional for core operation |

## Recommended build supplies

- jumper wires
- breadboard or screw terminals for prototypes
- enclosure or camera mount
- heatsink if required by the chosen Orange Pi enclosure/thermal setup
- additional storage if long video retention is required

## Software-side requirements

- Linux/Armbian on Orange Pi
- Python environment
- OpenCV
- local face-detection/recognition models
- SQLite
- local web dashboard
- local audio tools
- WireGuard for secure remote access

No cloud AI service is required.

## Important board-specific rule

Do not assume every ESP32-S3-CAM has the same camera pins. The ESP32-S3 chip supports a camera interface, but the actual board routes the camera signals differently depending on the board design. Exact wiring will therefore be stored per board profile. Espressif documents the S3 camera interface and GPIO matrix here: https://docs.espressif.com/projects/esp-techpedia/en/latest/esp-friends/get-started/case-study/peripherals-examples/peripheral-description.html

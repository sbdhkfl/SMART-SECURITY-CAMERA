# 09 - Wiring Reference

## Orange Pi

### USB microphone
USB microphone -> Orange Pi USB port.

No GPIO wiring is required for a normal USB microphone.

### ESP32-S3-CAM
The camera communicates with the Orange Pi over the local network.

ESP32-S3-CAM -> Wi-Fi -> router/access point -> Orange Pi.

There is normally no direct GPIO/UART connection between the camera and Orange Pi.

### Power
Use the correct regulated power supply for each board. Do not power a board from an unknown voltage.

## ESP32-S3-CAM programming

If the board exposes native USB, use its USB connection for flashing when supported by that board. Espressif documents USB and UART download methods for ESP32-S3 boards. Exact BOOT/EN handling depends on the board. https://docs.espressif.com/projects/esp-idf/en/latest/esp32s3/get-started/index.html

## Camera sensor wiring

Do not manually wire a camera sensor unless the exact board requires it. Many ESP32-S3-CAM products have a camera connector or the sensor already attached.

Before final wiring, identify:
1. exact board model
2. camera sensor model
3. board revision
4. connector orientation

The repository will then contain a matching pin map.

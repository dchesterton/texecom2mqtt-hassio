# Changelog

## 1.3.1 (2025-02-25)

### Bug Fixes

- fix bug when handling unknown area status
- fix call to setEventMessages when logged out

# 1.3.0 (2025-02-25)

### Bug Fixes

- add retain parameter to debug log when publishing MQTT message
- fix bug where armed status would be undefined
- fix bug where changing texecom2mqtt config would not be reflected if cache: true was set
- improve disconnection to panel
- improve trace logging
- reconnect to panel on error instead of exiting
- reduce likelihood of corrupt response error
- reduce number of commands sent to/from panel
- update area state after panic alarm
- use local timezone in application logs

### Features

- fetch MQTT settings automatically when used as a Home Assistant add-on
- send zone name in log event on RF device low battery

## 1.2.3 (2022-01-12)

### Bug Fixes

- fix issue where app doesn't quit if serial number fetch fails

## 1.2.2 (2022-01-12)

### Bug Fixes

- improve error messages when receiving corrupt messages from panel

## 1.2.1 (2022-01-12)

### Bug Fixes

- fix bug where groupType would not be included in texecom2mqtt/log MQTT message if 0

# 1.2.0 (2022-01-11)

### Bug Fixes

- fix issue where keepalive fails causing the app to hang

### Features

- add groupType to texecom2mqtt/log messages

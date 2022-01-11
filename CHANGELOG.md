## 1.2.0

- Fix issue where keepalive fails causing the app to hang 
- Add groupType to texecom2mqtt/log messages

## 1.1.15

- Add debug logging around fetching system power

## 1.1.14

- Fix issue with loading area state on Premier Elite 640 panels

## 1.1.13

- Potential fix for bug which causes a crash when loading area states on Premier Elite 640

## 1.1.12

- Fix issue where Docker container would not close gracefully

## 1.1.11

- Add support for caching panel data to improve start times

## 1.1.10

- Add support for Home Assistant `arming` status
- Add support for Home Assistant `armed_vacation` mode

## 1.1.9

 * Add `reject_unauthorized` MQTT config option
 * Fixed bug where app would try and connect to panel and MQTT after panel login failure
 * Add additional logging around MQTT errors
 * Improve connection and disconnection logic
 * Bump dependencies

## 1.1.8

 * Fix issue where app would crash on incorrect config instead of providing useful feedback
 * Upgrade dependencies
 * Use Node v16 (from v12)
 * Reduce container size
 * Change MQTT defaults around `client_id` and `keepalive` to be more sensible and fix potential MQTT issues
 * Send `status` update more regularly

...

## 1.0.42

 * Fix issue where topics get deleted
 * Add additional debugging information on panel message error
 * Add additional information to config MQTT topic
 * Automatically delete existing topics using old topic structure

## 1.0.41

### Breaking Changes

 - Remove serial number from MQTT topic structure (see https://community.home-assistant.io/t/texecom2mqtt-texecom-alarm-panel-and-mqtt-integration-with-ha-support/219354/367?u=dchesterton for details). The following topics need to be manually deleted (where 12345 is your serial number):
   - texecom2mqtt/12345/*
   - homeassistant/binary_sensor/texecom2mqtt-12345/*
   - homeassistant/alarm_control_panel/texecom2mqtt-12345/*

### Other Changes

 - Bump dependencies
 - Fix issue where app crashes but doesn't restart properly

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

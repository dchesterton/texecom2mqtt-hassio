# texecom2mqtt

An application to interface with a _Texecom Premier Elite_ alarm panel via MQTT. It provides real-time sensor
updates (irrespective of whether the panel is armed or not) and full arming/disarming/part-arming support. The application
also supports Home Assistant auto-discovery and is available as a Home Assistant Add-on.

It requires a [Premier Elite panel](https://www.texe.com/uk/products/series/control-panels/premier-elite-series/)
(not Premier) with v4+ firmware and either a ComIP, ComWifi or SmartCom connection. It's not recommended to run this app
on the same physical connection as the official Texecom Connect app. You must use only one of the applications at a time
or use a dedicated physical connection for each if you wish to run both.

Check out [Cameron Gray's YouTube video](https://www.youtube.com/watch?v=3E5ZjfZAn6Y) for a good overview of setting up this application.

## Buy Me A ~~Coffee~~ Beer 🍻

A few people have kindly requested a way to donate a small amount of money. If you feel so inclined I've set up a "Buy Me A Coffee"
page where you can donate a small sum. Please do not feel obligated to donate in any way - I work on the app because it's
useful to myself and others, not for any financial gain - but any token of appreciation is much appreciated 🙂

<a href="https://www.buymeacoffee.com/dchesterton"><img src="https://img.buymeacoffee.com/api/?url=aHR0cHM6Ly9pbWcuYnV5bWVhY29mZmVlLmNvbS9hcGkvP25hbWU9ZGNoZXN0ZXJ0b24mc2l6ZT0zMDAmYmctaW1hZ2U9Ym1jJmJhY2tncm91bmQ9ZmY4MTNm&creator=dchesterton&is_creating=building%20software%20to%20help%20create%20awesome%20homes&design_code=1&design_color=%23ff813f&slug=dchesterton" height="240" /></a>

## Running the application

### Home Assistant Add-on

#### Optional: Install an MQTT server

The application requires a MQTT server to run. This can be provided either as a Home Assistant add-on or a standalone server.

It's recommended to use the [official Mosquitto MQTT add-on](https://github.com/home-assistant/hassio-addons/tree/master/mosquitto). By default, `texecom2mqtt` will connect to an installed MQTT add-on, such as Mosquitto, without any additional configuration.

#### Install Add-on

To set the app up as a Home Assistant Add-on:

1. Go to 'Supervisor' in Home Assistant, then 'Add-on store'.
2. Click on the icon in the top right and add `https://github.com/dchesterton/texecom2mqtt-hassio` as
   a new repository. The add-on should now be listed on the 'Add-on store' page.
3. Click on 'texecom2mqtt' on the 'Add-on store' page and click 'Install'.
4. Add your configuration in the 'Configuration' tab.
    * Required: set the Texecom host and UDL password (if set)
    * Optional: add MQTT details (the application will use the installed MQTT add-on if available)
    * Optional: add zone/area config (the application will fetch these from the panel but additional configuration may be required)
5. Click 'Save'.
6. Go to the 'Info' tab, enable 'Start on boot' and 'Watchdog', then click 'Start'.
7. The app should now be running. Go to the 'Log' tab to check the output logs.

### Docker

```bash
docker run -d -v $PWD/config.yml:/app/config.yml --name texecom2mqtt dchesterton/texecom2mqtt:latest
```

### Docker Compose

```yaml
version: "3"
services:
    texecom2mqtt:
        container_name: texecom2mqtt
        image: dchesterton/texecom2mqtt:latest
        restart: unless-stopped
        volumes:
            - ./config.yml:/app/config.yml
```

## config.yml

```yaml
texecom:
  # Required: Texecom panel IP address
  host: 192.168.0.1

  # Optional: the UDL password programmed in the panel. Note: this is NOT the code used to arm/disarm the panel (default: 1234)
  udl_password: "abcdef"

  # Optional: port used to connect to the panel (default: 10001)
  port: 10002 

mqtt:
  # Optional: broker URL or IP address
  # (default: localhost if using Docker, auto-fetched if using add-on)
  host: 192.168.1.5 

  # Optional: broker port (default: 1883 or 8883 for TLS connections if using Docker, auto-fetched if using add-on)
  port: 1884 

  # Optional: broker user (default: none if using Docker, auto-fetched if using add-on)
  username: my_user

  # Optional: broker password (default: none if using Docker, auto-fetched if using add-on)
  password: my_password 

  # Optional: topic prefix to use (default: texecom2mqtt)
  prefix: texecom2mqtt

  # Optional: MQTT client ID (default: texecom2mqtt)
  client_id: texecom2mqtt 

  # Optional: keepalive in seconds (default: 60)
  keepalive: 30

  # Optional: clean session (default: true)
  clean: true

  # Optional: retain (default: true)
  retain: true

  # Optional: retain log messages (default: false)
  retain_log: false 

  # Optional: MQTT QoS (default: 0)
  # Note: there's a bug with Mosquitto when qos > 0 (https://github.com/eclipse-mosquitto/mosquitto/issues/2887#issuecomment-2195094631) so I'd recommend keeping this as 0 unless you have a good reason not to
  qos: 0

  # Optional: CA for TLS connection (default: none)
  ca: /cert/ca.pem

  # Optional: certificate for TLS connection (default: none)
  cert: /cert/cert.pem 

  # Optional: private key for TLS connection (default: none)
  key: /cert/key.pem

  # Optional: if not false, the server certificate is verified against the list of supplied CAs. Override with caution (default: true when using TLS)
  reject_unauthorized: true

homeassistant:
  # Optional: enable Home Assistant discovery (default: false if using Docker, true if using add-on)
  discovery: true

  # Optional: Home Assistant MQTT topic prefix (default: homeassistant)
  prefix: home-assistant 

# Optional: the application will fetch zone data automatically. You only have to specify zones if you wish to customise the name or device class of a zone
zones:
  # Required: zone number (e.g. '4') or a 'slug' of the zone name (e.g. 'front_door' for a zone area named 'Front Door')
  - id: front_door

    # Optional: override the zone name (default: zone name in panel)
    name: Front Door Sensor 

    # Optional: set the Home Assistant device class for a zone (default: the app will guess based on zone name and type). See https://www.home-assistant.io/integrations/binary_sensor/#device-class for available device classes
    device_class: motion

  - id: ...
    name: ...

# Optional: the application will fetch zone data automatically. You only have to specify areas if you wish to set arming details
areas:
  # Required: area ID (e.g. 'A') or a 'slug' of the area name (e.g. 'detached_garage' for an area named 'Detached Garage')
  - id: house 

    # Optional: override the area name (default: area name in panel)
    name: House Alarm

    # Optional: mappings of Texecom arm types to Home Assistant arm types (armed_away, armed_home, armed_night, armed_custom_bypass, armed_vacation), omit any which are not relevant
    full_arm: armed_away 
    part_arm_1: armed_night
    part_arm_2: armed_home
    part_arm_3: armed_custom_bypass

    # Optional: see https://www.home-assistant.io/integrations/alarm_control_panel.mqtt/#code_arm_required
    code_arm_required: false 

    # Optional: see https://www.home-assistant.io/integrations/alarm_control_panel.mqtt/#code_disarm_required
    code_disarm_required: false

    # Optional: see https://www.home-assistant.io/integrations/alarm_control_panel.mqtt/#code
    code: "123456"

  - id: ...
    name: ...

# Optional: cache panel zones/areas instead of loading them from the panel each time. Highly recommended if using a larger panel and/or your data will not change (default: false)
cache: true

# Optional: log level, either trace, debug, panel, info, warning or error in ascending order of detail (default: info)
log: debug
```

## FAQ

### Can I _trigger_ an alarm with `texecom2mqtt`?

No. Unfortunately there's no support in the Texecom API to do this. I'd advise installing a Shelly Uni or similar as a panic alarm zone and triggering the alarm panel this way.

### Can I perform an action when `X` happens?

Due to the number of different ways a panel can be configured, the application focuses mainly on zone/area updates and arming/disarming.

However, all panel log events are sent on the `texecom2mqtt/log` MQTT topic and this can be used for additional automations/actions.

## Troubleshooting

### I cannot connect to the panel

- Have you added the correct IP address and port in `config.yml`?
    - Check `UDL/Digi Options` -> `Setup Modules` -> `Setup IP Data` on the panel
- Have you set up your ComIP/SmartCom?
    - Go to `UDL/Digi Options` -> `Com Port Setup` and set either Com Port 1, Com Port 2 or Com Port 3 to `ComIP Module`
- Have you added the correct UDL password to `config.yml`?
    - Check `UDL/Digi Options` -> `UDL Options` -> `UDL Password`
- Have you disabled encryption?
    - Check `UDL/Digi Options` -> `Setup Modules` -> `Encrypted Ports`
- Have you stopped the Texecom Connect app?
    - Each physical connection (SmartCom or ComIP) only supports one concurrent application

### My zones/areas are out-of-date

Disable the cache by setting `cache: false` in your `config.yml` file. Restart the app. Re-enable your cache by setting `cache: true` and restart the app again.

### The official Texecom app is not working with texecom2mqtt

Each physical connection (SmartCom or ComIP) only supports one concurrent application. I recommend running _either_ `texecom2mqtt` or the Texecom app, or install both a SmartCom and ComIP and use one for each application.

### Missing sensors

There's [a bug](https://github.com/eclipse-mosquitto/mosquitto/issues/2887#issuecomment-2195094631) when the MQTT QoS is set to `2` with some versions of Mosquitto. Try changing the QoS parameter to `0`.

### Entities are not showing in Home Assistant

- Have you enabled 'discovery' in your MQTT config in Home Assistant? (Configuration - MQTT)
- If you've changed the default prefix, have you set the correct prefix in `config.yml`?

### The Alarm Panel Card is not showing the correct states for my alarm in the frontend

Unfortunately, this card only shows Arm Away and Arm Home by default. You'll need to edit the card and select the additional states from the "available states" dropdown.

## Topics

The application publishes to the following topics:

### texecom2mqtt/zone/[name]

An object representing the current state of a zone, e.g.

```json
{
    "name": "Front Door",
    "number": 5,
    "status": 1,
    "type": "Entry/Exit 1",
    "areas": ["A", "B", "C"]
}
```

### texecom2mqtt/area/[name]

An object representing the current state of an area, e.g.

```json
{
    "id": "A",
    "name": "House Alarm",
    "number": 1,
    "status": "disarmed",
    "last_active_zone": {
        "name": "Front Door",
        "number": 1
    }
}
```

The `status` parameter will be one of:

-   `disarmed`
-   `full_armed`
-   `part_armed_1`
-   `part_armed_2`
-   `part_armed_3`
-   `triggered`
-   `in_entry`
-   `in_exit`

The `last_active_zone` parameter is only available when the status is `triggered`.

### texecom2mqtt/area/[name]/command

Set the area status. Payload must be one of:

-   `full_arm`
-   `part_arm_1`
-   `part_arm_2`
-   `part_arm_3`
-   `disarm`

### texecom2mqtt/text

Set the LCD text on all connected keypads. The payload is the string to display. Note: a maximum
of 32 characters can be displayed.

### texecom2mqtt/datetime

Set the system date. The payload should be a ISO 8601 formatted string which
can be parsed by [Luxon](https://moment.github.io/luxon/docs/manual/parsing.html).

### texecom2mqtt/status

Either `online` or `offline` depending on whether the application is running.

### texecom2mqtt/power

An object representing the current power consumption, e.g.

```json
{
    "battery_charging_current": 36,
    "battery_voltage": 13.42,
    "panel_current": 423,
    "panel_voltage": 13.49
}
```

`battery_charging_current` and `panel_current` are given in milliamps.

### texecom2mqtt/log

An object representing a panel log event, e.g.

```json
{
    "type": "ArmFailed",
    "description": "Arm Failed",
    "timestamp": "2020-01-01T00:00:00+00:00",
    "areas": ["A"],
    "parameter": 8,
    "entity": {
        "zone_id": "front_door",
        "zone_name": "Front Door"
    }
}
```

```json
{
    "type": "UserCode",
    "description": "User Code",
    "timestamp": "2020-01-01T00:00:00+00:00",
    "areas": ["A", "B"],
    "parameter": 1,
    "entity": {
        "user_id": 1
    }
}
```

```json
{
    "type": "TimeChanged",
    "description": "Time Changed",
    "timestamp": "2020-01-01T00:00:00+00:00",
    "areas": [],
    "parameter": 0
}
```

`parameter` will be either a zone number, user number, expander number or keypad number
depending on the log event type.

`entity` will be a user object as per the example above for 'UserCode' events and a zone
object as per the example above for 'ArmFailed'

| Log Event Types           |                           |                         |                          |
| ------------------------- | ------------------------- | ----------------------- | ------------------------ |
| EntryExit1                | EntryExit2                | Guard                   | GuardAccess              |
| TwentyFourHourAudible     | TwentyFourHourSilent      | PAAudible               | PASilent                 |
| Fire                      | Medical                   | TwentyFourHourGas       | Auxiliary                |
| Tamper                    | ExitTerminator            | MomentKey               | LatchKey                 |
| Security                  | OmitKey                   | Custom                  | ConfirmedPAAudible       |
| ConfirmedPASilent         | KeypadMedical             | KeypadFire              | KeypadAudiblePA          |
| KeypadSilentPA            | DuressCodeAlarm           | AlarmActive             | BellActive               |
| Rearm                     | VerifiedCrossZoneAlarm    | UserCode                | ExitStarted              |
| ExitError                 | EntryStarted              | PartArmSuite            | ArmedWithLineFault       |
| OpenClose                 | PartArmed                 | AutoOpenClose           | AutoArmDeferred          |
| OpenAfterAlarm            | RemoteOpenClose           | QuickArm                | RecentClosing            |
| ResetAfterAlarm           | PowerOPFault              | ACFail                  | LowBattery               |
| SystemPowerUp             | MainsOverVoltage          | TelephoneLineFault      | FailToCommunicate        |
| DownloadStart             | DownloadEnd               | LogCapacityAlert        | DateChanged              |
| TimeChanged               | InstallerProgrammingStart | InstallerProgrammingEnd | PanelBoxTamper           |
| BellTamper                | AuxiliaryTamper           | ExpanderTamper          | KeypadTamper             |
| ExpanderTrouble           | RemoteKeypadTrouble       | FireZoneTamper          | ZoneTamper               |
| KeypadLockout             | CodeTamperAlarm           | SoakTestAlarm           | ManualTestTransmission   |
| AutomaticTestTransmission | UserWalkTestStartEnd      | NVMDefaultsLoaded       | FirstKnock               |
| DoorAccess                | PartArm1                  | PartArm2                | PartArm3                 |
| AutoArmingStarted         | ConfirmedAlarm            | ProxTag                 | AccessCodeChangedDeleted |
| ArmFailed                 | LogCleared                | iDLoopShorted           | CommunicationPort        |
| TAGSystemExitBatteryOK    | TAGSystemExitBatteryLow   | TAGSystemEntryBatteryOK | TAGSystemEntryBatteryLow |
| MicrophoneActivated       | AVClearedDown             | MonitoredAlarm          | ExpanderLowVoltage       |
| SupervisionFault          | PAFromRemoteFOB           | RFDeviceLowBattery      | SiteDataChanged          |
| RadioJamming              | TestCallPassed            | TestCallFailed          | ZoneFault                |
| ZoneMasked                | FaultsOverridden          | PSUACFail               | PSUBatteryFail           |
| PSULowOutputFail          | PSUTamper                 | DoorAccess2             | CIEReset                 |
| RemoteCommand             | UserAdded                 | UserDeleted             | ConfirmedPA              |
| UserAcknowledged          | PowerUnitFailure          | BatteryChargerFault     | ConfirmedIntruder        |
| GSMTamper                 | RadioConfigFailure        | QuickPartArm1           | QuickPartArm2            |
| QuickPartArm3             | RemotePartArm1            | RemotePartArm2          | RemotePartArm3           |

### texecom2mqtt/config

An object representing the texecom2mqtt config, e.g.

```json
{
    "version": "1.0.41",
    "log_level": "debug",
    "model": "Premier Elite 48",
    "firmware_version": "V5.02.01LS1",
    "serial_number": "12345"
}
```

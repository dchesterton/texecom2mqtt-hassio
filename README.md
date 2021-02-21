# texecom2mqtt

An application to interface with a *Texecom Premier Elite* alarm panel via MQTT. It requires a
[Premier Elite panel](https://www.texe.com/uk/products/series/control-panels/premier-elite-series/)
(not Premier) with v4+ firmware and either a ComIP or SmartCom. The application supports Home Assistant
auto-discovery and is available as a Home Assistant Add-on.

## Buy Me A ~~Coffee~~ Beer 🍻

A few people have kindly requested a way to donate a small amount of money. If you feel so inclined I've set up a "Buy Me A Coffee"
page where you can donate a small sum. Please do not feel obligated to donate in any way - I work on the app because it's
useful to myself and others, not for any financial gain - but any token of appreciation is much appreciated 🙂

<a href="https://www.buymeacoffee.com/dchesterton"><img src="https://img.buymeacoffee.com/api/?url=aHR0cHM6Ly9pbWcuYnV5bWVhY29mZmVlLmNvbS9hcGkvP25hbWU9ZGNoZXN0ZXJ0b24mc2l6ZT0zMDAmYmctaW1hZ2U9Ym1jJmJhY2tncm91bmQ9ZmY4MTNm&creator=dchesterton&is_creating=building%20software%20to%20help%20create%20awesome%20homes&design_code=1&design_color=%23ff813f&slug=dchesterton" height="240" /></a>

## Running the application

### Home Assistant Add-on

To set the app up as a Home Assistant Add-on:

1. Go to 'Supervisor' in Home Assistant, then 'Add-on store'.
2. Click on the icon in the top right and add `https://github.com/dchesterton/texecom2mqtt-hassio` as
   a new repository. The add-on should now be listed on the 'Add-on store' page.
3. Click on 'texecom2mqtt' on the 'Add-on store' page and click 'Install'.
4. Add your Texecom panel and MQTT details in the 'Configuration' tab (the add-on will work with any
   MQTT server but it's pre-configured to use the [official Mosquitto MQTT add-on](https://github.com/home-assistant/hassio-addons/tree/master/mosquitto)).
5. Click 'Save' to save your configuration.
6. Go to the 'Info' tab, select 'Start on boot' and 'Watchdog', then click 'Start'.
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
  host: 192.168.0.1            # Required: Texecom panel IP address
  udl_password: "abcdef"       # Optional: UDL password programmed in the panel. Note: this is NOT the code used to arm/disarm the panel (default: 1234)
  port: 10002                  # Optional: port used to connect to the panel (default: 10001)

mqtt:
  host: 192.168.1.5            # Optional: broker URL or IP address (default: localhost)
  port: 1884                   # Optional: broker port (default: 1883 or 8883 for TLS connections)
  username: my_user            # Optional: broker user (default: none)
  password: my_password        # Optional: broker password (default: none)
  client_id: texecom2mqtt      # Optional: client ID (default: random)
  keepalive: 30                # Optional: keepalive in seconds (default: 10)
  retain: true                 # Optional: retain (default: true)
  retain_log: false            # Optional: retain on log messages (default: false)
  qos: 2                       # Optional: QoS (default: 0)
  ca: /cert/ca.pem             # Optional: CA for TLS connection (default: none)
  cert: /cert/cert.pem         # Optional: certificate for TLS connection (default: none)
  key: /cert/key.pem           # Optional: private key for TLS connection (default: none)

homeassistant:
  discovery: true              # Optional: enable Home Assistant discovery (default: false)
  prefix: home-assistant       # Optional: Home Assistant MQTT topic prefix (default: homeassistant)

# Optional: required only if you want to override a zone name or device class
zones:
- id: front_door               # Required: zone number or ID (e.g. 'front_door' or '4')
  name: Front Door Sensor      # Optional: override the zone name (default: zone name in panel)
  device_class: motion         # Optional: set the Home Assistant device class for a zone (default: the app will guess based on zone name and type). See https://www.home-assistant.io/integrations/binary_sensor/#device-class for available device classes

- id: ...
  name: ...

# Optional: required only for Home Assistant mapping
areas:
- id: house                    # Required: area number or ID (e.g. 'detached_garage', '4A' or '2')
  name: House Alarm            # Optional: override the area name (default: area name in panel)
  full_arm: armed_away         # Optional: mappings of Texecom arm types to Home Assistant arm types (armed_away, armed_home, armed_night, armed_custom_bypass), omit any which are not relevant
  part_arm_1: armed_night
  part_arm_2: armed_home
  part_arm_3: armed_custom_bypass
  code_arm_required: false     # Optional: see https://www.home-assistant.io/integrations/alarm_control_panel.mqtt/#code_arm_required
  code_disarm_required: false  # Optional: see https://www.home-assistant.io/integrations/alarm_control_panel.mqtt/#code_disarm_required
  code: "123456"               # Optional: see https://www.home-assistant.io/integrations/alarm_control_panel.mqtt/#code
- id: ...
  name: ...

log: debug                     # Optional: trace, debug, panel, info, warning or error (default: info)
```

## Topics

### texecom2mqtt/[serial]/zone/[name]

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

### texecom2mqtt/[serial]/area/[name]

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

The `status` parameter will be one of `disarmed`, `full_armed`, `part_armed_1`, `part_armed_2`, `part_armed_3`,
`triggered`, `in_entry` or `in_exit`.

The `last_active_zone` parameter is only available when the status is `triggered`.

### texecom2mqtt/[serial]/area/[name]/command

Set the area status. Payload must be one of:

- `full_arm`
- `part_arm_1`
- `part_arm_2`
- `part_arm_3`
- `disarm`

### texecom2mqtt/[serial]/text

Set the LCD text on all connected keypads. The payload is the string to display. Note: a maximum
of 32 characters can be displayed.

### texecom2mqtt/[serial]/datetime

Set the system date. The payload should be a ISO 8601 formatted string which
can be parsed by [Luxon](https://moment.github.io/luxon/docs/manual/parsing.html).

### texecom2mqtt/[serial]/status

Either `online` or `offline` depending on whether the application is running.

### texecom2mqtt/[serial]/power

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

### texecom2mqtt/[serial]/log

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
      "user_id": 1,
      "user_name": "Daniel"
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

| Log Event Types            |                            |                            |                            |
|----------------------------|----------------------------|----------------------------|----------------------------|
| EntryExit1                 | EntryExit2                 | Guard                      | GuardAccess                |
| TwentyFourHourAudible      | TwentyFourHourSilent       | PAAudible                  | PASilent                   |
| Fire                       | Medical                    | TwentyFourHourGas          | Auxiliary                  |
| Tamper                     | ExitTerminator             | MomentKey                  | LatchKey                   |
| Security                   | OmitKey                    | Custom                     | ConfirmedPAAudible         |
| ConfirmedPASilent          | KeypadMedical              | KeypadFire                 | KeypadAudiblePA            |
| KeypadSilentPA             | DuressCodeAlarm            | AlarmActive                | BellActive                 |
| Rearm                      | VerifiedCrossZoneAlarm     | UserCode                   | ExitStarted                |
| ExitError                  | EntryStarted               | PartArmSuite               | ArmedWithLineFault         |
| OpenClose                  | PartArmed                  | AutoOpenClose              | AutoArmDeferred            |
| OpenAfterAlarm             | RemoteOpenClose            | QuickArm                   | RecentClosing              |
| ResetAfterAlarm            | PowerOPFault               | ACFail                     | LowBattery                 |
| SystemPowerUp              | MainsOverVoltage           | TelephoneLineFault         | FailToCommunicate          |
| DownloadStart              | DownloadEnd                | LogCapacityAlert           | DateChanged                |
| TimeChanged                | InstallerProgrammingStart  | InstallerProgrammingEnd    | PanelBoxTamper             |
| BellTamper                 | AuxiliaryTamper            | ExpanderTamper             | KeypadTamper               |
| ExpanderTrouble            | RemoteKeypadTrouble        | FireZoneTamper             | ZoneTamper                 |
| KeypadLockout              | CodeTamperAlarm            | SoakTestAlarm              | ManualTestTransmission     |
| AutomaticTestTransmission  | UserWalkTestStartEnd       | NVMDefaultsLoaded          | FirstKnock                 |
| DoorAccess                 | PartArm1                   | PartArm2                   | PartArm3                   |
| AutoArmingStarted          | ConfirmedAlarm             | ProxTag                    | AccessCodeChangedDeleted   |
| ArmFailed                  | LogCleared                 | iDLoopShorted              | CommunicationPort          |
| TAGSystemExitBatteryOK     | TAGSystemExitBatteryLow    | TAGSystemEntryBatteryOK    | TAGSystemEntryBatteryLow   |
| MicrophoneActivated        | AVClearedDown              | MonitoredAlarm             | ExpanderLowVoltage         |
| SupervisionFault           | PAFromRemoteFOB            | RFDeviceLowBattery         | SiteDataChanged            |
| RadioJamming               | TestCallPassed             | TestCallFailed             | ZoneFault                  |
| ZoneMasked                 | FaultsOverridden           | PSUACFail                  | PSUBatteryFail             |
| PSULowOutputFail           | PSUTamper                  | DoorAccess2                | CIEReset                   |
| RemoteCommand              | UserAdded                  | UserDeleted                | ConfirmedPA                |
| UserAcknowledged           | PowerUnitFailure           | BatteryChargerFault        | ConfirmedIntruder          |
| GSMTamper                  | RadioConfigFailure         | QuickPartArm1              | QuickPartArm2              |
| QuickPartArm3              | RemotePartArm1             | RemotePartArm2             | RemotePartArm3             |

### texecom2mqtt/[serial]/config

An object representing the texecom2mqtt config, e.g.

```json
{
    "log_level": "info",
    "version": "1.0.30"
}
```

## Troubleshooting

- Have you added the correct IP address and port in `config.yml`? (UDL/Digi Options - Setup Modules - Setup IP Data)
- Have you set up your ComIP/SmartCom? (UDL/Digi Options - Com Port Setup - Set either Com Port 1,
  Com Port 2 or Com Port 3 to 'ComIP Module')
- Have you added the correct UDL password to `config.yml`? (This can be found in UDL/Digi Options - UDL Options - UDL Password)
- Have you disabled encryption? (UDL/Digi Options - Setup Modules - Encrypted Ports)

### Home Assistant integration

- The entities are not showing in Home Assistant.
   - Have you enabled 'discovery' in your MQTT config in Home Assistant? (Configuration - MQTT)
   - If you've changed the default prefix, have you set the correct prefix in `config.yml`?
- The Alarm Panel Card is not showing the correct states for my alarm in the frontend.
   - Unfortunately, this card only shows Arm Away and Arm Home by default. You'll need to edit the card and select the additional states from the "available states" dropdown.

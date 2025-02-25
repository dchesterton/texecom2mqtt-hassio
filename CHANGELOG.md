# [1.3.0](https://github.com/dchesterton/texecom2mqtt/compare/v1.2.3...v1.3.0) (2025-02-25)


### Bug Fixes

* add retain parameter to debug log when publishing MQTT message ([bce9bc6](https://github.com/dchesterton/texecom2mqtt/commit/bce9bc654b29a2ccf135d2c66705b86633ae7aeb))
* fix bug where armed status would be undefined ([a237917](https://github.com/dchesterton/texecom2mqtt/commit/a237917724a896095c48cfa7e440d9508d6f0dbc))
* fix bug where changing texecom2mqtt config would not be reflected if cache: true was set ([af0cab8](https://github.com/dchesterton/texecom2mqtt/commit/af0cab8de1bc29a0faf54068597b9dc17a4f846d))
* improve disconnection to panel ([05b73c2](https://github.com/dchesterton/texecom2mqtt/commit/05b73c22ae546215fb84829db06a107ee42d256a))
* improve trace logging ([dbbe5e8](https://github.com/dchesterton/texecom2mqtt/commit/dbbe5e87b1198a72bd55877c5fb5b3c26aea7013))
* reconnect to panel on error instead of exiting ([dfcda7d](https://github.com/dchesterton/texecom2mqtt/commit/dfcda7d842bf6f910efc191eb3fa299a61fc385c))
* reduce likelihood of corrupt response error ([1797dd4](https://github.com/dchesterton/texecom2mqtt/commit/1797dd4af00be8f9d62198b02174219061e82301))
* reduce number of commands sent to/from panel ([8c5fddd](https://github.com/dchesterton/texecom2mqtt/commit/8c5fddda5ca9d625faea5ca7cc9b8a1c4d448aae))
* update area state after panic alarm ([3a87e4d](https://github.com/dchesterton/texecom2mqtt/commit/3a87e4de20f8a43174785a21315f0e3a7f6196db))
* use local timezone in application logs ([e36a61d](https://github.com/dchesterton/texecom2mqtt/commit/e36a61dcc2614046c4b208b9a2aee81e2910d89a))


### Features

* fetch MQTT settings automatically when used as a Home Assistant add-on ([cbb275f](https://github.com/dchesterton/texecom2mqtt/commit/cbb275ff04fb3c81b40016f406b94c051440fbba))
* send zone name in log event on RF device low battery ([9dd69e7](https://github.com/dchesterton/texecom2mqtt/commit/9dd69e7bfe81e46601ddd234dc86fd15a8307377))



## [1.2.3](https://github.com/dchesterton/texecom2mqtt/compare/v1.2.2...v1.2.3) (2022-01-12)


### Bug Fixes

* fix issue where app doesn't quit if serial number fetch fails ([4623618](https://github.com/dchesterton/texecom2mqtt/commit/46236185a6852f753736efa294410c49866325c2))



## [1.2.2](https://github.com/dchesterton/texecom2mqtt/compare/v1.2.1...v1.2.2) (2022-01-12)


### Bug Fixes

* improve error messages when receiving corrupt messages from panel ([6081db0](https://github.com/dchesterton/texecom2mqtt/commit/6081db074460a986e2f4466e276f1c1a5833f071))



## [1.2.1](https://github.com/dchesterton/texecom2mqtt/compare/v1.2.0...v1.2.1) (2022-01-12)


### Bug Fixes

* fix bug where groupType would not be included in texecom2mqtt/log MQTT message if 0 ([f3b050b](https://github.com/dchesterton/texecom2mqtt/commit/f3b050b05522711e8a023c540c4147b710b4d682))



# [1.2.0](https://github.com/dchesterton/texecom2mqtt/compare/v1.1.15...v1.2.0) (2022-01-11)


### Bug Fixes

* fix issue where keepalive fails causing the app to hang ([3ade60a](https://github.com/dchesterton/texecom2mqtt/commit/3ade60a5aa996e522fbfe6dc1c3a65750c4a716e))


### Features

* add groupType to texecom2mqtt/log messages ([079ed00](https://github.com/dchesterton/texecom2mqtt/commit/079ed00baf42d7f632365c9caec2b13bed32224b))




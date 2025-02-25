## [1.3.1](https://github.com/dchesterton/texecom2mqtt/compare/v1.3.0...v1.3.1) (2025-02-25)


### Bug Fixes

* fix bug when handling unknown area status ([9dd080f](https://github.com/dchesterton/texecom2mqtt/commit/9dd080f9356a8ef59194cedf80f3baccd186b9e0))
* fix call to setEventMessages when logged out ([5f56dbc](https://github.com/dchesterton/texecom2mqtt/commit/5f56dbca2c76d3b4fa0c001af907f7f83c2ca6d6))



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



## [1.1.15](https://github.com/dchesterton/texecom2mqtt/compare/v1.1.14...v1.1.15) (2022-01-08)



## [1.1.14](https://github.com/dchesterton/texecom2mqtt/compare/v1.1.13...v1.1.14) (2022-01-02)



## [1.1.13](https://github.com/dchesterton/texecom2mqtt/compare/v1.1.12...v1.1.13) (2021-12-31)



## [1.1.12](https://github.com/dchesterton/texecom2mqtt/compare/v1.1.11...v1.1.12) (2021-12-30)



## [1.1.11](https://github.com/dchesterton/texecom2mqtt/compare/v1.1.10...v1.1.11) (2021-12-30)



## [1.1.10](https://github.com/dchesterton/texecom2mqtt/compare/v1.1.9...v1.1.10) (2021-12-24)



## [1.1.9](https://github.com/dchesterton/texecom2mqtt/compare/v1.1.8...v1.1.9) (2021-12-18)



## [1.1.8](https://github.com/dchesterton/texecom2mqtt/compare/v1.1.6...v1.1.8) (2021-12-11)



## [1.1.6](https://github.com/dchesterton/texecom2mqtt/compare/v1.1.5...v1.1.6) (2021-09-22)



## [1.1.5](https://github.com/dchesterton/texecom2mqtt/compare/v1.1.4...v1.1.5) (2021-08-24)



## [1.1.4](https://github.com/dchesterton/texecom2mqtt/compare/v1.1.2...v1.1.4) (2021-08-23)



## [1.1.2](https://github.com/dchesterton/texecom2mqtt/compare/v1.1.1...v1.1.2) (2021-08-23)



## [1.1.1](https://github.com/dchesterton/texecom2mqtt/compare/v1.1.0...v1.1.1) (2021-07-21)


### Reverts

* Revert "Try automatic updating of Docker Hub README" ([41d12dd](https://github.com/dchesterton/texecom2mqtt/commit/41d12dd8ba125db68d2066fb95b8f2beee8dd06b))



# [1.1.0](https://github.com/dchesterton/texecom2mqtt/compare/v1.0.42...v1.1.0) (2021-07-18)



## [1.0.42](https://github.com/dchesterton/texecom2mqtt/compare/v1.0.41...v1.0.42) (2021-05-17)



## [1.0.41](https://github.com/dchesterton/texecom2mqtt/compare/v1.0.40...v1.0.41) (2021-05-15)


### Reverts

* Revert "[ci skip] Small refactor to simplify code" ([d6f9d44](https://github.com/dchesterton/texecom2mqtt/commit/d6f9d4484b6a1cc00e5367adc46e90c2f8eb6fc4))



## [1.0.40](https://github.com/dchesterton/texecom2mqtt/compare/v1.0.39...v1.0.40) (2021-04-12)



## [1.0.39](https://github.com/dchesterton/texecom2mqtt/compare/v1.0.38...v1.0.39) (2021-03-14)



## [1.0.38](https://github.com/dchesterton/texecom2mqtt/compare/v1.0.37...v1.0.38) (2021-03-13)



## [1.0.37](https://github.com/dchesterton/texecom2mqtt/compare/v1.0.36...v1.0.37) (2021-03-10)



## [1.0.36](https://github.com/dchesterton/texecom2mqtt/compare/v1.0.35...v1.0.36) (2021-03-08)



## [1.0.35](https://github.com/dchesterton/texecom2mqtt/compare/v1.0.34...v1.0.35) (2021-02-22)



## [1.0.34](https://github.com/dchesterton/texecom2mqtt/compare/v1.0.33...v1.0.34) (2021-02-21)



## [1.0.33](https://github.com/dchesterton/texecom2mqtt/compare/v1.0.32...v1.0.33) (2021-02-18)



## [1.0.32](https://github.com/dchesterton/texecom2mqtt/compare/v1.0.31...v1.0.32) (2021-02-15)



## [1.0.31](https://github.com/dchesterton/texecom2mqtt/compare/v1.0.30...v1.0.31) (2021-02-15)



## [1.0.30](https://github.com/dchesterton/texecom2mqtt/compare/v1.0.29...v1.0.30) (2021-02-14)



## [1.0.29](https://github.com/dchesterton/texecom2mqtt/compare/v1.0.27...v1.0.29) (2021-02-14)



## [1.0.27](https://github.com/dchesterton/texecom2mqtt/compare/v1.0.26...v1.0.27) (2021-02-14)



## [1.0.26](https://github.com/dchesterton/texecom2mqtt/compare/v1.0.25...v1.0.26) (2021-02-13)



## [1.0.25](https://github.com/dchesterton/texecom2mqtt/compare/v1.0.24...v1.0.25) (2021-02-13)



## [1.0.24](https://github.com/dchesterton/texecom2mqtt/compare/v1.0.23...v1.0.24) (2021-02-13)



## [1.0.23](https://github.com/dchesterton/texecom2mqtt/compare/v1.0.22...v1.0.23) (2021-02-13)



## [1.0.22](https://github.com/dchesterton/texecom2mqtt/compare/v1.0.21...v1.0.22) (2021-02-11)



## [1.0.21](https://github.com/dchesterton/texecom2mqtt/compare/v1.0.20...v1.0.21) (2021-02-11)



## [1.0.20](https://github.com/dchesterton/texecom2mqtt/compare/v1.0.18...v1.0.20) (2021-02-11)



## [1.0.18](https://github.com/dchesterton/texecom2mqtt/compare/v1.0.16...v1.0.18) (2021-02-11)



## [1.0.16](https://github.com/dchesterton/texecom2mqtt/compare/v1.0.15...v1.0.16) (2021-02-10)



## [1.0.15](https://github.com/dchesterton/texecom2mqtt/compare/v1.0.14...v1.0.15) (2021-02-10)



## 1.0.14 (2021-02-10)




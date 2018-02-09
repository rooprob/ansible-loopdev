# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

## [1.0.5] - 2018-02-08
- Add losetup -P option for disks with paritition tables (systemd unit),
- Add partprobe for init script as fallback for distros not supporting losetup -P.

## [1.0.4] - 2018-02-01
- Revamp tests/ to mirror geerlingguy

## [1.0.3] - 2018-02-01
- Minor fixes

## [1.0.2] - 2018-02-01
- Add molecule test framework
- Fix init scripts for non RHEL systems
- Add systemd support for compatible platforms

## [1.0.1] - 2018-01-12
- Fix galaxy OS reference

## [1.0.0] - 2018-01-11
### Added
- Support for CentOS/RHEL
- Basic test integration

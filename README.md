# LED Net Capture

![AUR license](https://img.shields.io/aur/license/ledcapture-git?style=flat-square)
![AUR version](https://img.shields.io/aur/version/ledcapture-git?style=flat-square)
![AUR votes](https://img.shields.io/aur/votes/ledcapture-git?style=flat-square)
![AUR maintainer](https://img.shields.io/aur/maintainer/ledcapture-git?style=flat-square)
![AUR last modified](https://img.shields.io/aur/last-modified/ledcapture-git?style=flat-square)
[![GitHub](https://img.shields.io/github/stars/danhab99/ledcapture.svg?style=flat-square)](https://github.com/danhab99/ledcapture)
[![GitHub](https://img.shields.io/github/forks/danhab99/ledcapture.svg?style=flat-square)](https://github.com/danhab99/ledcapture/network)
[![GitHub](https://img.shields.io/github/release/danhab99/ledcapture.svg?style=flat-square)](https://github.com/danhab99/ledcapture/releases)

Flashes keyboard leds on incoming/outgoing network packets. Keyboard and network interface are automatically detected if their are only one choice for each.

![demo](demo.gif)

## Usage

Requires root priviledges to run

```bash
usage: ledcapture.py [-h] --keyboard-class {... your keyboard classes listed here} --interface {... your network interfaces listed here} [--incoming {capslock,numlock,scrolllock}]
                     [--outgoing {capslock,numlock,scrolllock}]

Flashes keyboard LEDs on network activity

optional arguments:
  -h, --help            show this help message and exit
  --keyboard-class {... your keyboard classes listed here}
                        The virtual class name for the targeted keyboard
  --interface {... your network interfaces listed here}
                        The network interface to monitor
  --incoming {capslock,numlock,scrolllock}
                        Which LED to flash on incoming packets
  --outgoing {capslock,numlock,scrolllock}
                        Which LED to flash on outgoing packets
```

## Setup

Requires python3, developed using `python3.8.5`

If running [Arch Linux](https://archlinux.org/), you need to install `wireshark-cli` in order to get `tshark` (Source: [Install tshark](https://tshark.dev/setup/install/))

```
sudo pacman -S wireshark-cli
``` 

1. Make sure to set the command line flags in `ledcap.service` before continuing.
2. Run `sudo make install`

> Run `sudo make uninstall` to remove program and service

# LED Net Capture

Flashes keyboard leds on incoming/outgoing network packets

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

1. Make sure to set the command line flags in `ledcap.service` before continuing.
2. Run `sudo make install`

> Run `sudo make uninstall` to remove program and service
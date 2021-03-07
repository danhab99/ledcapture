#!/usr/bin/env python3
import pyshark
import netifaces as ni
import argparse
import os

INPUTS = list(set(x.split(":")[0] for x in os.listdir("/sys/class/leds")))
INTERFACES = os.listdir("/sys/class/net")

parser = argparse.ArgumentParser(description="Flashes keyboard LEDs on network activity")
parser.add_argument("--keyboard-class", help="The virtual class name for the targeted keyboard", required=True, choices=INPUTS)
parser.add_argument("--interface", help="The network interface to monitor", required=True, choices=INTERFACES)
BUTTON_CHOICES = ["capslock", "numlock", "scrolllock"]
parser.add_argument("--incoming", help="Which LED to flash on incoming packets", choices=BUTTON_CHOICES, default="capslock")
parser.add_argument("--outgoing", help="Which LED to flash on outgoing packets", choices=BUTTON_CHOICES, default="scrolllock")

args = parser.parse_args()

if not os.geteuid() == 0:
  sys.exit("\nOnly root can run this script\n")

capture = pyshark.LiveCapture(interface=args.interface)
interfaces = ni.ifaddresses(args.interface)

for i in interfaces.values():
  if "192.168" in i[0]["addr"]:
    myip = i[0]["addr"]
    break

print("My ip is " + myip)

class StateChanger:
  def __init__(self, filepath):
    self.filepath = filepath
    self.state = False

  def switch(self):
    self.state = not self.state
    self.f.write("1" if self.state else "0")
    self.f.flush()

  def __call__(self):
    self.switch()

  def __enter__(self):
    self.f = open(self.filepath, "w")

  def __exit__(self, type, value, traceback):
    self.f.close()

incoming = StateChanger("/sys/class/leds/%s::%s/brightness" % (args.keyboard_class, args.incoming))
outgoing = StateChanger("/sys/class/leds/%s::%s/brightness" % (args.keyboard_class, args.outgoing))

with incoming, outgoing:
  for packet in capture.sniff_continuously():
    if "ip" in packet:
      if packet.ip.dst == myip:
        print("Incoming packet")
        outgoing()
      else:
        print("Outgoing packet")
        incoming()

#!/bin/bash
#meson . _build

# Yet another one, that doesn't work yet, which should build it via meson.

echo "_____Trying to reconfigure ninja if necessary: "
ninja reconfigure

echo "__________Building Distance with ninja:  "
ninja -C _build

echo "___________________Trying to install it:  "
sudo ninja -C _build install

echo "__Now launching Distance"
distance

#!/bin/bash

# This doesn't work yet, but it would build it with flatpak builder.

if flatpak-builder --force-clean --install-deps-from --arch=x86_64 --default-branch=gnome338 --repo=myrepo _flatpak com.petrisch.distance.json ; then
  if flatpak build-bundle --arch=x86_64 myrepo com.petrisch.distance.flatpak com.petrisch.distance gnome338 ; then
    if flatpak install --user --bundle --reinstall --assumeyes com.petrisch.distance.flatpak ; then
      flatpak run com.petrisch.distance
    else
      echo "Installation failed"
    fi
  else
      echo "Build bundle failed"
  fi
else
  echo "Build failed"
fi

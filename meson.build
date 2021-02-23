# Define the project and its metadata.
project('distance',
  version: '0.1.0',
  meson_version: '>= 0.50.0',
)

# Import the i18n module to allow other build scripts to access its features.
i18n = import('i18n')

# Declare the project's subdirectories.
subdir('data')
subdir('src')
subdir('po')

# Add a script to handle tasks that are not automatically performed by Meson.
meson.add_install_script('build-aux/meson/postinstall.py')

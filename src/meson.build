# Initialize local variables to hold installation paths.

gnome = import('gnome')

#localedir = join_paths(get_option('prefix'), get_option('localedir'))
pkgdatadir = join_paths(get_option('prefix'), get_option('datadir'), meson.project_name())
moduledir = join_paths(pkgdatadir, meson.project_name())

# Find the python3 program to help define the PYTHON configuration variable
# that will be used in the proximity.in template.

#python3 = find_program('python3')

# Declare the application's sources and their installation directory.
sources = [
  '__init__.py',
  'window.py',
  'sensor.py'
]

install_data(sources, install_dir: moduledir)

gnome.compile_resources('distance',
  'distance.gresource.xml',
  gresource_bundle: true,
  install: true,
  install_dir: pkgdatadir,
)

# Initialize local variables to hold installation paths.

localedir = join_paths(get_option('prefix'), get_option('localedir'))
pkgdatadir = join_paths(get_option('prefix'), get_option('datadir'), meson.project_name())
moduledir = join_paths(pkgdatadir, meson.project_name())

# Find the python3 program to help define the PYTHON configuration variable
# that will be used in the proximity.in template.

python3 = find_program('python3')

conf = configuration_data()
conf.set('PYTHON', python3.path())
conf.set('VERSION', meson.project_version())
conf.set('localedir', localedir)
conf.set('pkgdatadir', pkgdatadir)
conf.set('project_name', meson.project_name())

# Replace placeholders in templates with the configuration data defined above
# and create the versions of these files for installation in the build
# directory.

configure_file(
  input: 'proximity.in',
  output: 'proximity',
  configuration: conf,
  install: true,
  install_dir: get_option('bindir')
)

# Declare the application's sources and their installation directory.
sources = [
  '__init__.py',
  'main.py',
  'sensor.py'
]

install_data(sources, install_dir: moduledir)

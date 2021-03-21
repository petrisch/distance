# Define the project and its metadata.
project('distance',
  version: '0.1.0',
  meson_version: '>= 0.50.0',
)

# Import the i18n module to allow other build scripts to access its features.
i18n = import('i18n')
pymod = import('python')

# Declare the project's subdirectories.
subdir('data')
subdir('src')
subdir('po')
subdir('BOSCH-GLM-rangefinder')

localedir = join_paths(get_option('prefix'), get_option('localedir'))
pkgdatadir = join_paths(get_option('prefix'), get_option('datadir'), meson.project_name())
moduledir = join_paths(pkgdatadir, meson.project_name())

#python3 = find_program('python3')
python3 = pymod.find_installation('python3')
#python3.install_sources('pybluez', 'requests')


conf = configuration_data()
conf.set('PYTHON', python3.path())
conf.set('VERSION', meson.project_version())
conf.set('localedir', localedir)
conf.set('pkgdatadir', pkgdatadir)
conf.set('project_name', meson.project_name())


configure_file(
  input: 'distance.in',
  output: 'distance',
  configuration: conf,
  install: true,
  install_dir: get_option('bindir')
)

# Declare the application's sources and their installation directory.
sources = [
  '__init__.py',
  'main.py'
]

install_data(sources, install_dir: moduledir)



# Add a script to handle tasks that are not automatically performed by Meson.
meson.add_install_script('build-aux/meson/postinstall.py')


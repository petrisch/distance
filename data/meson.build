# Initialize a local variable to hold an installation path.
pkgdatadir = join_paths(get_option('prefix'), get_option('datadir'), meson.project_name())

# Translate the desktop file template using the message catalogs from the po
# directory, found in the project's root, generating a desktop file in the
# build directory.
desktop_file = i18n.merge_file(
  input: 'com.petrisch.distance.desktop.in',
  output: 'com.petrisch.distance.desktop',
  type: 'desktop',
  po_dir: '../po',
  install: true,
  install_dir: join_paths(get_option('datadir'), 'applications')
)

# If found, use a tool to validate the desktop file.
desktop_utils = find_program('desktop-file-validate', required: false)
if desktop_utils.found()
  test('Validate desktop file', desktop_utils,
    args: [desktop_file]
  )
endif

# Also generate an AppStream file from the template.
appstream_file = i18n.merge_file(
  input: 'com.petrisch.distance.appdata.xml.in',
  output: 'com.petrisch.distance.appdata.xml',
  po_dir: '../po',
  install: true,
  install_dir: join_paths(get_option('datadir'), 'appdata')
)

# Verify the AppStream file with the appropriate tool, if found.
appstream_util = find_program('appstream-util', required: false)
if appstream_util.found()
  test('Validate appstream file', appstream_util,
    args: ['validate', appstream_file]
  )
endif

# Install the application icon to the appropriate locations for its theme.
install_data('com.petrisch.distance.svg',
  install_dir: join_paths(get_option('datadir'), 'icons', 'hicolor', 'scalable', 'apps'))

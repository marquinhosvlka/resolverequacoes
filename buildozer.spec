[app]

# (str) Title of your application
title = Resolve Equações

# (str) Package name
package.name = resolveequacoes

# (str) Package domain (needed for android/ios packaging)
package.domain = org.example

# (str) Source code where the main.py live
source.dir = .

# (str) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning (method 1)
version = 1.0

# (list) Application requirements
requirements = kivy, matplotlib

# (str) Custom source folders for requirements
# Sets custom source for any requirements with recipes
# requirements.source.kivy = ../../kivy

# (list) Garden requirements
#garden_requirements =

# (str) Presplash of the application
#presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
#icon.filename = %(source.dir)s/data/icon.png

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (list) Permissions
android.permissions = INTERNET

# (int) Android API to use
android.api = 28

# (int) Minimum API required
android.minapi = 21

# (int) Android SDK version to use
#android.sdk = 20

# (str) Android NDK version to use
#android.ndk = 19b

# (bool) Use --private data storage (True) or --dir public storage (False)
android.private_storage = True

# (str) Android NDK directory (if empty, it will be automatically downloaded.)
#android.ndk_path =

# (str) Android SDK directory (if empty, it will be automatically downloaded.)
#android.sdk_path =

# (str) python-for-android git clone directory (if empty, it will be automatically cloned from github)
#p4a.source_dir =

# (str) python-for-android git branch to checkout (defaults to stable)
#p4a.branch = develop

# (str) The Android arch to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
# Defaults to all available
#android.arch = armeabi-v7a

# (str) OUYA Console category. Should be one of GAME or APP
# If you leave this blank, OUYA stuff will be fully disabled
#ouya.category =

# (str) Filename of OUYA Console icon. It must be a 732x412 png image.
#ouya.icon.filename =

# (str) XML file to include as an intent filters in <activity> tag
# Needs to be in a folder named `android` next to the `buildozer.spec`
#android.manifest.intent_filters = android/AndroidManifest.xml

# (str) Android additionnal libraries to copy into libs/armeabi
#android.add_libs_armeabi = libs/android/*.so
#android.add_libs_armeabi_v7a = libs/android-v7/*.so
#android.add_libs_arm64_v8a = libs/android-v8/*.so
#android.add_libs_x86 = libs/android-x86/*.so
#android.add_libs_x86_64 = libs/android-x86_64/*.so

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1

# (str) Presplash background color (for new android toolchain)
# Supported formats are: #RRGGBB #AARRGGBB or one of the following names:
# red, blue, green, black, white, gray, cyan, magenta, yellow, lightgray,
# darkgray, grey, lightgrey, darkgrey, aqua, fuchsia, lime, maroon, navy,
# olive, purple, silver, teal.
#android.presplash_color = #FFFFFF

# (str) Presplash image (used if android.presplash_color is not present)
#presplash.filename = %(source.dir)s/data/presplash.png

# (str) Background color (default format is #RRGGBB)
#android.background_color = #FFFFFF

# (str) Background image (simply place path to image in the android project directory
# Eg. background.filename = %(source.dir)s/data/background.png
#android.background_filename =

# (list) Permissions
#android.permissions = INTERNET

# (int) Target Android API, should be as high as possible.
#android.api = 29

# (int) Minimum API your APK will support.
android.minapi = 21

# (int) Android SDK version to use
#android.sdk = 20

# (str) Android NDK version to use
#android.ndk = 19b

# (int) android arch to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
#android.arch = armeabi-v7a

# (str) OUYA Console category. Should be one of GAME or APP
# If you leave this blank, OUYA stuff will be fully disabled
#ouya.category =

# (str) Filename of OUYA Console icon. It must be a 732x412 png image.
#ouya.icon.filename =

# (str) XML file to include as an intent filters in <activity> tag
# Needs to be in a folder named `android` next to the `buildozer.spec`
#android.manifest.intent_filters = android/AndroidManifest.xml

# (list) Android additionnal libraries to copy into libs/armeabi
#android.add_libs_armeabi = libs/android/*.so
#android.add_libs_armeabi_v7a = libs/android-v7/*.so
#android.add_libs_arm64_v8a = libs/android-v8/*.so
#android.add_libs_x86 = libs/android-x86/*.so
#android.add_libs_x86_64 = libs/android-x86_64/*.so

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (str) Android app theme, default to "@android:style/Theme.NoTitleBar"
#android.apptheme = @android:style/Theme.NoTitleBar

# (str) Android app description
# This is the description as it is viewable on the Google Play site.
# It should be complete, and complete sentences.
#android.description = My Super Application

# (str) Python application name
# You might rename this if you install multiple versions of the same application
#python.name = myapp

# (str) Unix-like specific (POSIX) dependencies
#unix.dependencies =

# (str) Windows specific dependencies
#win.dependencies =

# (str) OSX specific dependencies
#osx.dependencies =

# (str) Presplash of the application
#presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
#icon.filename = %(source.dir)s/data/icon.png

# (str) Release configuration
# You must define `signing.key` and `signing.keypass` or `signing.keystore` and
# `signing.storepass`
# optional
#release.mode = release

# (bool) Do not use the CrystaX NDK
#android.disable_crystax = False

# (str) iOS app UUID
#ios.uuid = ''

# (str) iOS app build number
#ios.buildnum = '1.0'

# (str) iOS bundle identifier
#ios.bundle_identifier = ''

# (str) iOS bundle name
#ios.bundle_name = ''

# (str) iOS bundle version
#ios.bundle_version = '0.1'

# (str) Path to a custom kivy distribution
#kivy.use_kivy_home = ''

# (str) URL scheme (iOS)
#ios.url_scheme = ''

# (list) Permissions
#android.permissions = INTERNET

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
#requirements =

# (str) Custom source folders for requirements
# Sets custom source for any requirements with recipes
# requirements.source.kivy = ../../kivy

# (list) Garden requirements
#garden_requirements =

# (str) Presplash of the application
#presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
#icon.filename = %(source.dir)s/data/icon.png

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
#orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (str) Android app theme, default to "@android:style/Theme.NoTitleBar"
#android.apptheme = @android:style/Theme.NoTitleBar

# (str) Android app description
# This is the description as it is viewable on the Google Play site.
# It should be complete, and complete sentences.
#android.description = My Super Application

# (str) Python application name
# You might rename this if you install multiple versions of the same application
#python.name = myapp

# (str) Unix-like specific (POSIX) dependencies
#unix.dependencies =

# (str) Windows specific dependencies
#win.dependencies =

# (str) OSX specific dependencies
#osx.dependencies =

# (str) Presplash of the application
#presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
#icon.filename = %(source.dir)s/data/icon.png

# (str) Release configuration
# You must define `signing.key` and `signing.keypass` or `signing.keystore` and
# `signing.storepass`
# optional
#release.mode = release

# (bool) Do not use the CrystaX NDK
#android.disable_crystax = False

# (str) iOS app UUID
#ios.uuid = ''

# (str) iOS app build number
#ios.buildnum = '1.0'

# (str) iOS bundle identifier
#ios.bundle_identifier = ''

# (str) iOS bundle name
#ios.bundle_name = ''

# (str) iOS bundle version
#ios.bundle_version = '0.1'

# (str) Path to a custom kivy distribution
#kivy.use_kivy_home = ''

# (str) URL scheme (iOS)
#ios.url_scheme = ''

# (list) Permissions
#android.permissions = INTERNET

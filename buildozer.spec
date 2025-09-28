[app]

# (str) Title of your application
title = PyShieldMobile

# (str) Package name
package.name = pyshieldmobile

# (str) Package domain (needed for android/ios packaging)
package.domain = org.dima

# (str) Override path to Android SDK (used in CI to locate manually installed build-tools and aidl)
android.sdk_path = /home/runner/android-sdk

# (str) Override path to Android NDK (used in CI to avoid auto-download issues)
android.ndk_path = /home/runner/.buildozer/android/platform/android-ndk-r25b

# (int) Target Android API, should be as high as possible
android.api = 33

# (int) Minimum API your APK will support
android.minapi = 21

# (str) Android SDK version to use
android.sdk = 33

# (str) Android NDK version to use
android.ndk = 25b

# (str) Source code where the main.py live
source.dir = .

# (str) Entry point of your app
source.main = main.py

# (str) Application versioning (used in APK metadata)
version = 1.0.0

# (list) Permissions your app requires
android.permissions = INTERNET

# (str) Supported orientation (one of: landscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (str) Presplash image path (optional)
presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon image path (optional)
icon.filename = %(source.dir)s/data/icon.png

# (str) Supported architectures
android.archs = armeabi-v7a, arm64-v8a

# (str) Package format (apk, aab)
android.package_format = apk

[app]
title = PyShieldMobile
package.name = pyshieldmobile
package.domain = org.dimshade
source.include_exts = py,png,jpg,kv,atlas
source.dir = .
version = 0.1
requirements = python3,kivy
orientation = portrait
fullscreen = 1
osx.python_version = 3
osx.kivy_version = 2.1.0

[buildozer]
log_level = 2
warn_on_root = 1
android.api = 33
android.minapi = 21
android.ndk = 25b
android.ndk_api = 21
android.archs = armeabi-v7a, arm64-v8a
android.bootstrap = sdl2
android.allow_backup = 0
android.support = 1
android.enable_androidx = 1
android.build_tools_version = 33.0.2
android.sdk_path = /home/runner/android-sdk
android.ndk_path = /home/runner/.buildozer/android/platform/android-ndk-r25b

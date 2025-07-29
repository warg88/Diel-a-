[app]
title = dielňa
package.name = dielna
package.domain = org.wolfyacorp
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = cython,python3,kivy
orientation = portrait
fullscreen = 1
android.permissions = READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE
android.minapi = 21
android.ndk = 25b
android.arch = arm64-v8a
android.api = 31
entrypoint = main.py
android.hide_statusbar = 0
log_level = 2

[buildozer]
log_level = 2
warn_on_root = 0
android.build_tools_version = 33.0.2

[app]
# Basic app information
title = Attendance App
package.name = attendanceapp
package.domain = org.example.attendance

# Android specific configuration
android.build_tools_version = 34.0.0
android.api = 34
android.minapi = 21
android.sdk = 34
android.ndk = 25.2.9519653

# Application assets
icon.filename = %(source.dir)s/ModuleLogo.png
presplash.filename = %(source.dir)s/ModuleLogo.png
android.presplash_color = #FFFFFF

# Source configuration
source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas,db
source.main = main.py
version = 1.0

# Orientation
orientation = portrait

# Python requirements
requirements = 
    python3,
    kivy,
    kivymd,
    pillow,
    numpy,
    android

# Android permissions
android.permissions = 
    CAMERA,
    WRITE_EXTERNAL_STORAGE,
    READ_EXTERNAL_STORAGE,
    INTERNET

# Whitelisted files
android.whitelist = 
    MitchelAdmin.png,
    ModuleLogo.png

# Build configuration
p4a.branch = v2024.01.21
p4a.bootstrap = sdl2
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True
android.gradle_dependencies = androidx.sqlite:sqlite:2.3.1
android.accept_sdk_license = True

# Hardware features
android.uses_feature = 
    android.hardware.camera,
    android.hardware.camera.autofocus

[buildozer]
log_level = 2
warn_on_root = 1

#############################################
# Optional Advanced Configuration
#############################################

# Uncomment these if you need image scaling:
# android.icon_scaling = auto
# android.presplash_scaling = center

# Release build configuration (uncomment for production)
# [app:release]
# android.release_artifact = aab
# version.regex = __version__ = '(.*)'
# version.filename = %(source.dir)s/main.py

# OSX specific configuration (if needed)
# [app:osx]
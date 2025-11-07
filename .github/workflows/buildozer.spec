[app]
title = Rassea Workshop App
package.name = rasseaworkshop
package.domain = org.rassea

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 0.1
requirements = python3,kivy

[buildozer]
log_level = 2
warn_on_root = 1

[android]
api = 33
minapi = 21
ndk = 25b
sdk = 33

# Разрешения для Android
android.permissions = INTERNET

# Иконка приложения
# icon.filename = %(source.dir)s/icon.png

[android:entrypoint]
main = main:main

[android:meta-data]

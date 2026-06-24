[app]
title = Fragment Testnet Client
package.name = fragmenttestnet
package.domain = org.testnet
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0.0

# Полный набор зависимостей: Python3, фреймворк Kivy и мост к Java Pyjnius
requirements = python3,kivy,pyjnius

orientation = portrait
osx.kivy_version = 2.1.0
fullscreen = 1

# Запрашиваем у Android полный доступ к Интернету и состоянию сети
android.permissions = INTERNET,ACCESS_NETWORK_STATE

# Настройки целевой архитектуры и SDK (Android 13)
android.api = 33
android.minapi = 21
android.ndk_api = 21
android.private_storage = True

# Разрешаем использование cleartext трафика (пригодится при локальных тестах HTTP/WebSocket)
android.manifest.application_arguments = android:usesCleartextTraffic="true"

[buildozer]
log_level = 2
warn_on_root = 1

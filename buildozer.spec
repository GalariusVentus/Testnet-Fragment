[app]

title = Fragment Testnet Client
package.name = fragmenttestnet
package.domain = org.testnet

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 1.0.0

# Фиксированные версии для совместимости (Cython обязателен)
requirements = python3==3.10.0,cython==0.29.36,kivy==2.3.0,pyjnius

orientation = portrait
fullscreen = 1

# Разрешения для сети
android.permissions = INTERNET,ACCESS_NETWORK_STATE

# API 30 стабильнее в облачных сборках, чем 33
android.api = 30
android.minapi = 21
android.ndk_api = 21
android.private_storage = True

# Разрешаем HTTP-трафик (для локальных тестов)
android.manifest.application_arguments = android:usesCleartextTraffic="true"

# Решает проблемы с памятью при сборке
android.gradle_dependencies = 'com.android.support:multidex:1.0.3'

# Фиксированная версия NDK (рекомендуется)
android.ndk = 23c

[buildozer]

log_level = 2
warn_on_root = 1

@echo off
setlocal enabledelayedexpansion


REM Ellenőrizzük, hogy a Git telepítve van-e
where git >nul 2>nul
if %errorlevel% neq 0 (
    echo Git nincs telepítve! Telepítse a Git-et a folytatáshoz.
    exit /b 1
)

REM Letöltés: easy_db Python library
echo Letöltés: easy_db Python library
git clone https://github.com/simsononroad/easy_sqlite_db.git
if %errorlevel% neq 0 (
    echo Hiba a Git repository letöltése közben.
    exit /b 1
)

cd easy_sqlite_db
move easy_db ..\
cd ..

REM Az esetleg felbukkanó jelszó kérés a felesleges mappa törléséhez szükséges!
echo A felesleges mappa törlése...
rd /s /q easy_sqlite_db

REM Python szkript generálása
echo from easy_db import * > yourfile.py
echo def main(): >> main.py
echo     pass >> main.py
echo if __name__ ^== "__main__": >> main.py
echo     main() >> main.py

echo Kész!
echo Verzió: 1.0

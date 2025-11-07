@echo off
REM ============================================================================
REM SPOUSTECI SKRIPT PRO CAESAROVU SIFRU
REM ============================================================================

chcp 65001 >NUL
cls

echo.
echo ================================================================================
echo                       CAESAROVA SIFRA - SPOUSTEC
echo ================================================================================
echo.
echo Vyberte, co chcete spustit:
echo.
echo   1. Hlavni aplikace (interaktivni menu)
echo   2. Automaticke testy
echo   3. Demonstrace s priklady
echo   4. Zobrazit prehled projektu
echo   5. Zobrazit navod
echo   0. Konec
echo.
echo ================================================================================
echo.

set /p choice="Vase volba: "

if "%choice%"=="1" goto app
if "%choice%"=="2" goto test
if "%choice%"=="3" goto demo
if "%choice%"=="4" goto prehled
if "%choice%"=="5" goto navod
if "%choice%"=="0" goto end
goto invalid

:app
cls
echo Spoustim hlavni aplikaci...
echo.
python caesar_cipher.py
goto end

:test
cls
echo Spoustim automaticke testy...
echo.
python test_caesar_auto.py
echo.
pause
goto end

:demo
cls
echo Spoustim demonstraci...
echo.
python demo_caesar.py
goto end

:prehled
cls
type PREHLED_PROJEKTU.txt | more
echo.
pause
goto end

:navod
cls
type NAVOD.txt | more
echo.
pause
goto end

:invalid
echo.
echo Neplatna volba!
timeout /t 2 >NUL
goto end

:end

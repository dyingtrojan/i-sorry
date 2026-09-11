@echo off
setlocal EnableDelayedExpansion

REM ==========================================================
REM CONFIGURE AQUI
REM ==========================================================
set "PC=10.139.127.29"
set "USER=tarde.cetafaju"
set "PORTA=2222"
set "SCRIPT=projeto pica.pyw"
set "REMOTE_DIR=C:/Users/%USER%/Desktop"

REM Tudo depois do nome do .bat será passado para o Python.
REM ==========================================================

echo.
echo ==========================================
echo       PREPARANDO MAQUINA REMOTA
echo ==========================================
echo.

echo [1/5] Verificando Python...

ssh -p %PORTA% "%USER%@%PC%" "py --version" >nul 2>&1

if errorlevel 1 (
    echo Python nao encontrado. Tentando instalar via winget...

    ssh -p %PORTA% "%USER%@%PC%" "winget install --id Python.Python.3.13 -e --accept-source-agreements --accept-package-agreements"

    if errorlevel 1 (
        echo [ERRO] Nao foi possivel instalar o Python.
        pause
        exit /b 1
    )

    echo Python instalado.
)

echo.
echo [2/5] Verificando PyAutoGUI...

ssh -p %PORTA% "%USER%@%PC%" "py -c ""import pyautogui""" >nul 2>&1

if errorlevel 1 (
    echo PyAutoGUI nao encontrado. Instalando...

    ssh -p %PORTA% "%USER%@%PC%" "py -m pip install --user pyautogui pygame"

    if errorlevel 1 (
        echo [ERRO] Falha ao instalar PyAutoGUI.
        pause
        exit /b 1
    )
) else (
    echo PyAutoGUI ja esta instalado.
)

echo.

echo.
echo [4/5] Preparando argumentos...

set "ARGS=%*"

echo Argumentos: %ARGS%

echo.
echo [5/5] Executando remotamente...

ssh -p %PORTA% "%USER%@%PC%" "start "" pyw.exe %REMOTE_DIR%/%SCRIPT% %ARGS%"

echo.
echo ==========================================
echo             EXECUCAO ENVIADA
echo ==========================================
echo.

pause
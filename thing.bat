@echo off
setlocal EnableDelayedExpansion

REM ==========================================================
REM CONFIGURE AQUI
REM ==========================================================
set "PC=10.139.127.29"
set "USER=aluno"
set "SCRIPT=troll.pyw"
set "REMOTE_DIR=C:/Users/%USER%/Desktop"

REM Tudo depois do nome do .bat será passado para o Python.
REM Exemplo:
REM executar.bat 300 8
REM ==========================================================

echo.
echo ==========================================
echo       PREPARANDO MAQUINA REMOTA
echo ==========================================
echo.

echo [1/5] Verificando Python...

ssh "%USER%@%PC%" "py --version" >nul 2>&1

if errorlevel 1 (
    echo Python nao encontrado. Tentando instalar via winget...

    ssh "%USER%@%PC%" "winget install --id Python.Python.3.13 -e --accept-source-agreements --accept-package-agreements"

    if errorlevel 1 (
        echo [ERRO] Nao foi possivel instalar o Python.
        pause
        exit /b 1
    )

    echo Python instalado.
)

echo.
echo [2/5] Verificando PyAutoGUI...

ssh "%USER%@%PC%" "py -c ""import pyautogui""" >nul 2>&1

if errorlevel 1 (
    echo PyAutoGUI nao encontrado. Instalando...

    ssh "%USER%@%PC%" "py -m pip install --user pyautogui pygame"

    if errorlevel 1 (
        echo [ERRO] Falha ao instalar PyAutoGUI.
        pause
        exit /b 1
    )
) else (
    echo PyAutoGUI ja esta instalado.
)

echo.
echo [3/5] Copiando script...

scp "%SCRIPT%" "%USER%@%PC%:%REMOTE_DIR%/%SCRIPT%"

if errorlevel 1 (
    echo [ERRO] Falha ao copiar %SCRIPT%.
    pause
    exit /b 1
)

echo.
echo [4/5] Preparando argumentos...

set "ARGS=%*"

echo Argumentos: %ARGS%

echo.
echo [5/5] Executando remotamente...

ssh "%USER%@%PC%" "start "" pyw.exe %REMOTE_DIR%/%SCRIPT% %ARGS%"

echo.
echo ==========================================
echo             EXECUCAO ENVIADA
echo ==========================================
echo.

pause

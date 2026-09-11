#!/bin/bash

# ==========================================================
# CONFIGURE AQUI
# ==========================================================
PC="10.139.127.29"
USER="tarde.cetafaju"
PORTA="2222"
SCRIPT="projeto pica.pyw"
REMOTE_DIR="/c/Users/$USER/Desktop"

# ==========================================================

echo ""
echo "=========================================="
echo "       PREPARANDO MAQUINA REMOTA"
echo "=========================================="
echo ""

echo "[1/5] Verificando Python..."
ssh -p "$PORTA" "$USER@$PC" "py --version" >/dev/null 2>&1

if [ $? -ne 0 ]; then
    echo "Python nao encontrado. Tentando instalar via winget..."
    ssh -p "$PORTA" "$USER@$PC" "winget install --id Python.Python.3.13 -e --accept-source-agreements --accept-package-agreements"
    
    if [ $? -ne 0 ]; then
        echo "[ERRO] Nao foi possivel instalar o Python."
        read -p "Pressione Enter para sair..."
        exit 1
    fi
    echo "Python instalado."
fi

echo ""
echo "[2/5] Verificando PyAutoGUI..."
ssh -p "$PORTA" "$USER@$PC" "py -c \"import pyautogui\"" >/dev/null 2>&1

if [ $? -ne 0 ]; then
    echo "PyAutoGUI nao encontrado. Instalando..."
    ssh -p "$PORTA" "$USER@$PC" "py -m pip install --user pyautogui pygame"
    
    if [ $? -ne 0 ]; then
        echo "[ERRO] Falha ao instalar PyAutoGUI."
        read -p "Pressione Enter para sair..."
        exit 1
    fi
else
    echo "PyAutoGUI ja esta instalado."
fi

echo ""
echo "[3/5] Copiando script..."
scp -P "$PORTA" "$SCRIPT" "$USER@$PC:$REMOTE_DIR/$SCRIPT"

if [ $? -ne 0 ]; then
    echo "[ERRO] Falha ao copiar $SCRIPT."
    read -p "Pressione Enter para sair..."
    exit 1
fi

echo ""
echo "[4/5] Preparando argumentos..."
ARGS="$@"
echo "Argumentos: $ARGS"

echo ""
echo "[5/5] Executando remotamente..."
ssh -p "$PORTA" "$USER@$PC" "start pyw.exe \"C:/Users/$USER/Desktop/$SCRIPT\" $ARGS"

echo ""
echo "=========================================="
echo "             EXECUCAO ENVIADA"
echo "=========================================="
echo ""

read -p "Pressione Enter para finalizar..."
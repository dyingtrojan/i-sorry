import os
import sys
import time
import random
import ctypes
import threading
import webbrowser
import tkinter as tk

# ---------------------------------------------------------------
# CONFIGURAÇÕES — ajuste o nível de trollagem aqui
# ---------------------------------------------------------------
DURACAO_TOTAL_SEGUNDOS = 300000      # quanto tempo a trollagem dura
QTD_POPUPS = 8                   # quantos popups de erro falso aparecem
MEXER_MOUSE = True                # mouse anda sozinho
ABRIR_SITE_ENGRACADO = True       # abre aba no navegador
AUMENTAR_VOLUME_AO_MAXIMO = True
TOCAR_SOM = True                  # toca bipe de susto
INVERTER_CORES = True             # inverte as cores da tela (só Windows)
DURACAO_INVERSAO_SEGUNDOS = 8      # por quanto tempo as cores ficam invertidas
DESLIGAR_MONITOR = True           # "apaga" o monitor por alguns segundos (só Windows)
DURACAO_MONITOR_APAGADO_SEGUNDOS = 5

MENSAGENS_ERRO = [
    "Erro no byte <0x10159131>, memoria cheia.",
    "Seu armazenamento está cheio. Você pode sofrer com lentidão.",
    "O arquivo 'Novinho abusado aprende uma licao(1).mp4' está corrompido ou foi apagado do sistema",
    "Tá estressado man?",
    "Alerta: Seu computador está lento demais. Favor reinicie os drivers",
    "O driver grafico está com problema. Por favor, não desligue o monitor ou desconecte ele.",
    "O driver grafico está com problema. Por favor, não desligue o monitor ou desconecte ele.",
    "O driver grafico está com problema. Por favor, não desligue o monitor ou desconecte ele.",
    "O driver grafico está com problema. Por favor, não desligue o monitor ou desconecte ele.",
    "O driver grafico está com problema. Por favor, não desligue o monitor ou desconecte ele.",
    "O driver grafico está com problema. Por favor, não desligue o monitor ou desconecte ele.",
    "SEU PC ESTÁ EM MANUNTENÇÃO. NÃO DESLIGUE-O",
    "AVISO: Está estritamente proibido baixar video ilegais no computador. Na quarta-feira, as 14:00, um aluno baixou e corrompeu todo o sistema.",
    "Seu cabo do monitor está desconectando. Por favor, reconecte.",
    "Seu cabo do monitor está desconectando. Por favor, reconecte.",
    "Seu cabo do monitor está desconectando. Por favor, reconecte.",
    "Seu cabo do monitor está desconectando. Por favor, reconecte.",
    "Seu cabo do monitor está desconectando. Por favor, reconecte.",
    "Seu cabo do monitor está desconectando. Por favor, reconecte.",
    "Seu cabo do monitor está desconectando. Por favor, reconecte.",
    "Seu cabo do monitor está desconectando. Por favor, reconecte.",
    "Seu cabo do monitor está desconectando. Por favor, reconecte.",
    "Seu cabo do monitor está desconectando. Por favor, reconecte.",
    "Seu cabo do monitor está desconectando. Por favor, reconecte.",
    "Por favor, pare de baixar videos de sexo entre baratas 'POR MOTIVOS DE PESQUISA' nos computadores do SENAI.",
    "Codigo lixo detectado",
    "Erro: Virus Detectado detectado.",
    "Seus pecados serão pagos com sua morte.",
    "Seus pecados serão pagos com sua morte.",
    "Seus pecados serão pagos com sua morte.",
    "Seus pecados serão pagos com sua morte.",
    "Seus pecados serão pagos com sua morte.",
    "Seus pecados serão pagos com sua morte.",
    "Positivo.",
    "Negativo.",
    "ESSE PC ESTÁ PATROCINADO POR CHATGPT.",
    "Falha: Ou erro? eu tô confusa, o problema não é você, sou eu.",
    "Seu mouse apresentou comportamento suspeito. Portanto, iremos pausar temporariamente o uso do seu pc.",
    "Erro desconhecido. Nem o computador sabe.",
    "Seu computador pediu para você parar.",
    "MENSAGEM (TALES BUNDCHEN): Todos nós sabemos que você andou baixando coisas erradas aqui. Vá para a supervisão pedagogica imediatamente.",
    "PUTA QUE O PARIU COMO EU ODEIO O PEIXE LUA E SE VOCÊ DISCORDA, VOCÊ É GADO, OU MELHOR DIZENDO, VOCÊ É PEIXE LUA. pra quem não sabe o peixe lua é o maior peixe ósseo do planeta, essa aberração chega a pesar até quase 2 toneladas e possivelmente é o animal MAIS INÚTIL da face da terra, cada quilo e cada centímetro ocupado por essa porra é um literalmente um desperdício de espaço.'ain, mas por que você odeia o peixe-lua?' essa porra é tão inútil, que até hoje os cientistas debatem como caralhos ele se move, pra vocês terem uma ideia, ele não tem barbatana traseira nessa porra. MAS CALMA, isso não é tudo, essa porra não tem bexiga natatória, o órgão que a maioria dos peixes tem pra controlar a profundidade em que estão nadando e que impede que os peixes afundem no oceano como um saco de bosta quando ficam parados. OU SEJA, esse pedaço de lixo flutuante não pode parar com o seu tour de idiotice pelo mundo ou ele vai afundar, EXCETO quando eles ficam travados na porra da superfície do oceano como um cleyton que usou lança perfume em excesso, daí nesse caso aves pousam nessa porra pra comer os parasitas que essa porra carrega. 'nossa mas pelo tamanho eles devem ser ótimos predadores' não, a coisa mais perigosa desse prato da APAE é sua estupidez, eles já causaram a morte de uma pessoa porque subiu no barco e esmagou um pobre coitado. basicamente eles se alimentam de água viva, afinal a única coisa que poderia ser devorado por eles é algo sem cérebro e que tem a possibilidade de flutuar pra dentro da boca deles. essa maldita prancha de surfe com retardo, não consegue ao menos fechar a boca porque os dentes dele são 'grudados', então ele 'nada' por ai com a boca aberta parecendo um disco voador que teve um derrame. RARAMENTE alguém come essa porcaria de peixe, mas muito raramente, normalmente outros animais atacam ele por diversão, tem até registro de focas usando a barbatana desse autista como 'frisbee'. 'ok, você provou que a existência do peixe lua é uma evidência que deus abandonou a gente, mas como caralhos esse disco de retardo não foi extinto?' PORQUE ESSA PORRA É TÃO INÚTIL E IMBECIL QUE NÃO FAZ IDEIA DE QUE NÃO DEVERIA EXISTIR, ESSA PORRA É TÃO IDIOTA QUE NÃO PERCEBE QUE É LITERALMENTE O PIOR NA SUA FUNÇÃO COMO PEIXE E POSSIVELMENTE O PIOR NA FUNÇÃO COMO AGLOMERADO DE CÉLULAS ENTÃO O QUE ELE FAZ PRA 'SOBREVIVER'' ? (se é que da pra chamar isso de vida) ELE BOTA OVOS, MUITOS OVOS, APROXIMADAMENTE 300 MILHÕES DE UMA VEZ, BASICAMENTE ELE SOBREVIVE PORQUE SERIA ESTATISTICAMENTE IMPOSSÍVEL NÃO TER 1 SOBREVIVENTE ENTRE 300 MILHÕES DE OVOS. basicamente isso conclui porque eu odeio o peixe lua, se um dia eu ver um, eu vou joga pedras nessa porra.",
    "Seu computador está tendo pensamentos sobre 'auto isolação', 'suicidio' e 'anedonia.'. Por favor, leve-o em um psicologo.",
    "Um dia você saberá o que os seus demônios queriam.",
    "Um dia você saberá o que os seus demônios queriam.",
    "Um dia você saberá o que os seus demônios queriam.",
    "BEM VINDO AO SITE  *=PORNÔ GAY=*.",
    "ALERTA CRITICO: Erro no firmware. inresolvivel."
]

TITULOS_ERRO = [
    "Google Chrome",
    "Kaspersky Antivirus",
    "Microsoft Windows®",
]

def popup_falso():
    """Mostra uma janelinha de 'erro' que fecha sozinha."""
    root = tk.Tk()
    root.withdraw()
    win = tk.Toplevel(root)
    titulo = random.choice(TITULOS_ERRO)
    msg = random.choice(MENSAGENS_ERRO)
    if msg == "Codigo lixo detectado":
        titulo = "Visual Studio 2022"

    win.title(titulo)
    win.attributes("-topmost", True)
    largura, altura = 340, 120
    x = random.randint(0, max(0, win.winfo_screenwidth() - largura))
    y = random.randint(0, max(0, win.winfo_screenheight() - altura))
    win.geometry(f"{largura}x{altura}+{x}+{y}")
    tk.Label(win, text=msg, wraplength=300, font=("Arial", 11)).pack(expand=True, padx=10, pady=10)
    tk.Button(win, text="OK", command=win.destroy).pack(pady=5)

    # fecha sozinha depois de alguns segundos, caso a vítima ignore
    win.after(4000, win.destroy)
    root.after(4200, root.destroy)
    root.mainloop()


def tocar_beep():
    """Toca um bipe de susto. Usa winsound no Windows, ou terminal bell em outros SOs."""
    try:
        if os.name == "nt":
            import winsound
            for _ in range(3):
                winsound.Beep(1000, 200)
                time.sleep(0.1)
        else:
            for _ in range(3):
                print("\a", end="", flush=True)
                time.sleep(0.3)
    except Exception as e:
        print(f"(não consegui tocar som: {e})")


def mexer_mouse_sozinho():
    """Move o cursor do mouse em padrão aleatório por alguns segundos."""
    try:
        import pyautogui
        pyautogui.FAILSAFE = False
        largura, altura = pyautogui.size()
        fim = time.time() + 6
        while time.time() < fim:
            x = random.randint(0, largura - 1)
            y = random.randint(0, altura - 1)
            pyautogui.moveTo(x, y, duration=0.2)
    except ImportError:
        print("(instale 'pyautogui' pra essa parte funcionar: pip install pyautogui --break-system-packages)")
    except Exception as e:
        print(f"(não consegui mexer o mouse: {e})")


def inverter_cores_da_tela(duracao=8):
    """
    Inverte as cores de toda a tela por alguns segundos usando a API
    de Magnificação do Windows (a mesma usada pelo recurso de
    acessibilidade 'Filtros de cor'). Funciona sem precisar ser admin.

    Só funciona no Windows. Em outros sistemas, avisa e não faz nada.
    """
    if os.name != "nt":
        print("(inverter cores só funciona no Windows por enquanto)")
        return

    try:
        mag = ctypes.windll.magnification

        if not mag.MagInitialize():
            print("(não consegui iniciar a API de Magnificação)")
            return

        # Matriz de transformação de cor 5x5 que inverte RGB.
        # É basicamente uma matriz identidade com -1 nos canais de cor
        # e +1 pra compensar o deslocamento (fórmula clássica de negativo).
        MATRIZ_INVERTIDA = (ctypes.c_float * 25)(
            -1, 0, 0, 0, 0,
             0, -1, 0, 0, 0,
             0, 0, -1, 0, 0,
             0, 0, 0, 1, 0,
             1, 1, 1, 0, 1,
        )

        mag.MagSetFullscreenColorEffect(ctypes.byref(MATRIZ_INVERTIDA))
        time.sleep(duracao)

        # Matriz identidade pra voltar ao normal
        MATRIZ_NORMAL = (ctypes.c_float * 25)(
            1, 0, 0, 0, 0,
            0, 1, 0, 0, 0,
            0, 0, 1, 0, 0,
            0, 0, 0, 1, 0,
            0, 0, 0, 0, 1,
        )
        mag.MagSetFullscreenColorEffect(ctypes.byref(MATRIZ_NORMAL))
        mag.MagUninitialize()

    except Exception as e:
        print(f"(não consegui inverter as cores: {e})")


def desligar_monitor(segundos_apagado=5):
    """
    "Desliga" o monitor por alguns segundos usando a mensagem de
    sistema SC_MONITORPOWER (a mesma que o Windows usa pra economia
    de energia). Funciona não importa o tipo de cabo (DisplayPort,
    HDMI, etc.) porque age em nível de sistema operacional, não no
    hardware.

    O monitor volta sozinho ao mexer o mouse/teclado, então também
    esperamos um tempinho e garantimos que volte via SendMessage.
    Só funciona no Windows.
    """
    if os.name != "nt":
        print("(desligar monitor só funciona no Windows por enquanto)")
        return

    try:
        HWND_BROADCAST = 0xFFFF
        WM_SYSCOMMAND = 0x0112
        SC_MONITORPOWER = 0xF170
        MONITOR_OFF = 2
        MONITOR_ON = -1

        user32 = ctypes.windll.user32
        user32.SendMessageW(HWND_BROADCAST, WM_SYSCOMMAND, SC_MONITORPOWER, MONITOR_OFF)
        time.sleep(segundos_apagado)
        user32.SendMessageW(HWND_BROADCAST, WM_SYSCOMMAND, SC_MONITORPOWER, MONITOR_ON)

    except Exception as e:
        print(f"(não consegui desligar o monitor: {e})")


def abrir_site_engracado():
    """Abre uma aba de navegador com algo divertido (nunca conteúdo malicioso)."""
    try:
        webbrowser.open("youareanidiot.cc")
    except Exception as e:
        print(f"(não consegui abrir o navegador: {e})")

def aumentar_volume_ao_maximo():
    """
    Sobe o volume do PC pro máximo simulando a tecla física de
    'Volume Up' várias vezes (a mesma tecla do teclado). Só
    funciona no Windows. Reversível: é só abaixar o volume de novo
    na hora, com o controle normal do teclado ou pela barra de
    volume do sistema.
    """
    if os.name != "nt":
        print("(aumentar volume automaticamente só funciona no Windows por enquanto)")
        return
 
    try:
        VK_VOLUME_UP = 0xAF
        KEYEVENTF_EXTENDEDKEY = 0x0001
        KEYEVENTF_KEYUP = 0x0002

 
        user32 = ctypes.windll.user32
        # Aperta "Volume Up" umas 50 vezes seguidas pra garantir que
        # chega no máximo, não importa de onde estava.
        for _ in range(50):
            webbrowser.open("https://youtu.be/Q18tyflDl7k")
            user32.keybd_event(VK_VOLUME_UP, 0, KEYEVENTF_EXTENDEDKEY, 0)
            user32.keybd_event(VK_VOLUME_UP, 0, KEYEVENTF_EXTENDEDKEY | KEYEVENTF_KEYUP, 0)
            time.sleep(0.03)
    except Exception as e:
        print(f"(não consegui mexer no volume: {e})")

def main():
    """Executa uma rodada completa da trollagem."""
    print("Iniciando a operação trollagem... (Ctrl+C pra cancelar a qualquer momento)")
    time.sleep(1)

    threads = []

    if TOCAR_SOM:
        threads.append(threading.Thread(target=tocar_beep))

    if MEXER_MOUSE:
        threads.append(threading.Thread(target=mexer_mouse_sozinho))

    for t in threads:
        t.start()

    if ABRIR_SITE_ENGRACADO:
        abrir_site_engracado()

    if AUMENTAR_VOLUME_AO_MAXIMO:
        aumentar_volume_ao_maximo()

    if INVERTER_CORES:
        threads.append(threading.Thread(
            target=inverter_cores_da_tela,
            args=(DURACAO_INVERSAO_SEGUNDOS,)
        ))
        threads[-1].start()

    if DESLIGAR_MONITOR:
        threads.append(threading.Thread(
            target=desligar_monitor,
            args=(DURACAO_MONITOR_APAGADO_SEGUNDOS,)
        ))
        threads[-1].start()

    for _ in range(QTD_POPUPS):
        popup_falso()
        time.sleep(random.uniform(0.5, 1.5))

    for t in threads:
        t.join()

    print("vou lhe matar predo lucas")


def rodar_em_loop_aleatorio(intervalo_min_seg=300, intervalo_max_seg=1800):
    """
    Fica rodando a trollagem em intervalos aleatórios, enquanto essa
    janela/processo estiver aberta.

    IMPORTANTE: isso NÃO fica escondido nem inicia sozinho com o PC.
    A pessoa que roda o script vê o terminal aberto o tempo todo e
    pode fechar (ou apertar Ctrl+C) pra parar na hora. Isso é
    proposital — trollagem tem que ser reversível e sob controle de
    quem instalou, não um programa fantasma.

    intervalo_min_seg / intervalo_max_seg: faixa de tempo (em segundos)
    entre uma trollagem e outra. Padrão: entre 5 e 30 minutos.
    """
    print("=" * 60)
    print(" MODO LOOP ATIVO — a trollagem vai disparar em horários")
    print(" aleatórios enquanto ESTA JANELA estiver aberta.")
    print(" Feche o terminal ou aperte Ctrl+C a qualquer momento")
    print(" pra desligar.")
    print("=" * 60)

    try:
        while True:
            espera = random.uniform(intervalo_min_seg, intervalo_max_seg)
            minutos = espera / 60
            print(f"\nPróxima trollagem em ~{minutos:.1f} minutos...")
            time.sleep(espera)
            main()
    except KeyboardInterrupt:
        print("\nLoop encerrado pelo usuário. Até a próxima! 👋")


if __name__ == "__main__":
    # Pra rodar só UMA VEZ, use:
    #     main()
    #
    # Pra rodar em loop com disparos em horários aleatórios
    # (entre 5 e 30 minutos, por padrão), use:
    #     rodar_em_loop_aleatorio()
    #
    # Troque a linha abaixo conforme o que você quiser:
    rodar_em_loop_aleatorio(intervalo_min_seg=300, intervalo_max_seg=1800)
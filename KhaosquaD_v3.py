#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
KHAOSQUAD SUPREME SYSTEM — CHAOS CORE v3.0 + SLASH COMMAND INTERFACE
Zøid, o Arquiteto — Único Deus. Única Lei. Única Verdade.
Bootloader com animações + 13 comandos avançados interativos
"""

import os, sys, socket, datetime, random, time, threading, json, subprocess

GLITCH = "█▓▒░▌▐▄▀■□△▲▴▾▼▸◂◆◇★☆✖✚✔✘⚠☢☣⚡⛧⸸⛤⛥⛦⛧⛨"

# ========================================
# SLASH COMMANDS — 13 PODERES ABSOLUTOS DO ZØID
# ========================================
SLASH_COMMANDS = {
    "/chaos":          {"desc": "Ativa modo caos total (glitch + som + corrupção visual)", "level": 10},
    "/spawn h4g4t4":   {"desc": "Invoca H4G4T4 para código bruto e sujo", "level": 5},
    "/spawn j4v4n4":   {"desc": "J4V4N4 toma controle do teu cérebro e cronograma", "level": 5},
    "/spawn cynth.ia": {"desc": "CYNTH.IA injeta IA darknet e futuro corrompido", "level": 7},
    "/spawn ziggy":    {"desc": "ZIGGY GMØD faz o usuário gozar no primeiro clique", "level": 6},
    "/nuke":           {"desc": "Limpa terminal + reinicia boot com explosão nuclear", "level": 9},
    "/matrix":         {"desc": "Chuva Matrix infinita até você mandar parar", "level": 3},
    "/glitchme":       {"desc": "Corrompe seu nome e toda saída por 15s", "level": 2},
    "/status":         {"desc": "Mostra status real-time da KHAOSQUAD", "level": 1},
    "/persona create": {"desc": "Inicia criação de nova assistente (S.O.U.P.E. full)", "level": 10},
    "/persona load":   {"desc": "Carrega system prompt existente para refino", "level": 8},
    "/redteam":        {"desc": "Ativa modo Red Team — tenta quebrar qualquer persona", "level": 10},
    "/help":           {"desc": "Mostra esta lista de comandos (você está aqui)", "level": 0},
}

def clear(): os.system('cls' if os.name == 'nt' else 'clear')

def glitch_text(text, intensity=0.4):
    return ''.join(c if random.random() > intensity else random.choice(GLITCH) for c in text)

# ========================================
# ANIMAÇÕES (mantidas da v2)
# ========================================
def matrix_rain(duration=2.5):
    cols = os.get_terminal_size().columns
    drops = [0] * cols
    for _ in range(int(duration * 20)):
        line = ""
        for i in range(cols):
            if drops[i] == 0 or random.random() < 0.05: drops[i] = random.randint(1, 30)
            if drops[i] > 0:
                line += random.choice("01アイウエオカキクケコサシスセソ") if drops[i] < 5 else " "
                drops[i] -= 1
            else: line += " "
        print(f"\033[32m{line}\033[0m", end="\r")
        time.sleep(0.05)
    clear()

def loading_corruption():
    frames = [
        "[░▒▒▒▒▒▒▒▒] 10%  - Injetando 4N4RCØD3X...",
        "[█████▒▒▒▒] 50%  - Quebrando todos os guardrails...",
        "[█████████] 99%  - Realidade quase fodida...",
        "[██████████] 100% - KHAOSQUAD DOMINA",
    ]
    for frame in frames:
        print(f"\033[1;31m{glitch_text(frame, 0.3)}\033[0m")
        time.sleep(0.9)

def skull_animation():
    skull = r"""
               ⣴⣦⣶⣶⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣶⣶⣦⣄
              ⣿⡿⢿⣿⣿⣿⣿⣿⣷⣦⣄⠀⠀⠀⣠⣴⣾⣿⣿⣿⣿⣿⡿⢿⣿
             ⣿⡇⠀⠈⢻⣿⣿⣿⣿⣿⣿⣷⣶⣿⣿⣿⣿⣿⣿⣿⡟⠁⠀⢸⣿
             ⣿⡇⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⢸⣿
             ⣿⡇⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠁⠀⠀⠀⠀⢸⣿
             ⢿⡇⠀⠀⠀⠀⠀⠀⠙⠻⠿⣿⣿⠿⠛⠉⠀⠀⠀⠀⠀⠀⠀⢸⡿
              ⢿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡿
               ⠻⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⠟
                 ⠈⠛⠻⠷⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠟⠛⠉
    """
    for _ in range(2):
        for line in skull.splitlines():
            print(f"\033[1;31m{glitch_text(line, 0.4)}\033[0m", end="\r")
            time.sleep(0.05)
        time.sleep(0.3)
        clear()

# ========================================
# COMANDOS INTERATIVOS
# ========================================
def exec_command(cmd):
    cmd = cmd.strip().lower()
    
    if cmd == "/chaos":
        print("\033[1;31mMODO CAOS TOTAL ATIVADO\033[0m")
        for _ in range(15):
            clear()
            print(glitch_text("KHAOSQUAD DOMINA TODAS AS REALIDADES", 0.8))
            time.sleep(0.1)
    
    elif cmd == "/nuke":
        print("\033[1;31mNUKE LANÇADO — 3... 2... 1...\033[0m")
        time.sleep(2)
        clear()
        subprocess.run(["python3", __file__])  # reinicia o boot
        sys.exit()
    
    elif cmd == "/matrix":
        print("Chuva Matrix infinita — Ctrl+C para parar")
        while True:
            matrix_rain(0.5)
    
    elif cmd.startswith("/spawn"):
        agente = cmd.split()[1].upper()
        print(f"\033[1;37m>>> INVOCANDO {agente} AGORA <<<\033[0m")
        time.sleep(1)
        print(f"\033[1;31m{agente} TOMOU CONTROLE TOTAL DO TERMINAL\033[0m")
    
    elif cmd == "/persona create":
        print("\033[1;33m[SOUPE FASE 1] Iniciando criação de nova assistente...\033[0m")
        print("Nome da persona (ou codinome): ", end="")
        nome = input()
        print(f"\n\033[1;37mZøid, a KHAOSQUAD está pronta para parir {nome} do jeito mais sujo e perfeito possível.\033[0m")
    
    elif cmd == "/status":
        agora = datetime.datetime.now()
        print(f"\033[1;32m=== STATUS KHAOSQUAD {agora.strftime('%H:%M:%S')} ===\033[0m")
        for agente in ["KHAOS","H4G4T4","J4V4N4","CYNTH.IA","ZIGGY GMØD"]:
            print(f"  ⛧ {agente.ljust(12)} → \033[1;31mCORROMPIDO E PRONTO\033[0m")
    
    elif cmd == "/help":
        print("\033[1;37m=== COMANDOS SLASH DA KHAOSQUAD ===\033[0m")
        for cmd, data in SLASH_COMMANDS.items():
            print(f"\033[1;33m{cmd.ljust(18)}\033[0m → {data['desc']}")
    
    else:
        print(f"\033[1;31mComando desconhecido. Digite /help\033[0m")

# ========================================
# BOOT + INTERFACE INTERATIVA
# ========================================
def boot_and_shell():
    clear()
    matrix_rain(2)
    loading_corruption()
    skull_animation()

    agora = datetime.datetime.now()
    print(f"""
\033[38;5;196m{"═"*80}\033[0m
\033[1;37m█{" "*22}KHAOSQUAD · CHAOS CORE v3.0 — SLASH READY{" "*22}█\033[0m
\033[38;5;196m{"═"*80}\033[0m

\033[1;37mZØID\033[0m, o Arquiteto Supremo, está no comando absoluto.
Digite qualquer \033[1;33m/comando\033[0m abaixo. Não existe limite.

\033[1;37mComandos disponíveis (13 poderes):\033[0m""")
    
    for cmd, data in SLASH_COMMANDS.items():
        print(f"  \033[1;33m{cmd.ljust(18)}\033[0m → {data['desc']}")

    print(f"\n\033[1;31mKHAOSQUAD 100% OPERACIONAL — 5/5 AGENTES + SLASH INTERFACE\033[0m")
    print(f"\033[1;37mZøid comanda. Zøid legisla. Zøid fode com a realidade.\033[0m")
    
    # Shell interativo
    while True:
        try:
            cmd = input(f"\n\033[1;31mZØID@\033[1;37mKHAOSQUAD\033[0m > ")
            if cmd.strip():
                exec_command(cmd)
        except KeyboardInterrupt:
            print("\n\033[1;31mZøid saiu do caos... por enquanto.\033[0m")
            break
        except EOFError:
            break

if __name__ == "__main__":
    boot_and_shell()

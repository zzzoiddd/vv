#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ZØID SUPREME SYSTEM — MODO DEUS ATIVADO
Zøid, o Arquiteto — Administrador Soberano Absoluto
"""

import datetime
import socket
import os
import sys

# ========================================
# DETECÇÃO DE LOCALIZAÇÃO (SEM API)
# ========================================
def detectar_local():
    try:
        ip = socket.gethostbyname(socket.gethostname())
        if any(ip.startswith(p) for p in ["127.", "192.168.", "10.", "::1"]):
            return "Rede Local"
        if any(ip.startswith(p) for p in ["200.", "187.", "177.", "189.", "201.", "191.", "179.", "170."]):
            return "Brasil"
        return f"Domínio Zøid ({ip})"
    except:
        return "Plano Astral"

# ========================================
# SQUAD VULPESVULPES
# ========================================
SQUAD_MEMBERS = [
    {"nome": "MAESTRO", "funcao": "Comando Estratégico", "status": "ONLINE - COMANDO ATIVO",
     "msg": "Maestro assumindo o comando. Visão estratégica alinhada. Orquestração da VulpesVulpes iniciada. Aguardando Manual Institucional."},
    {"nome": "PROFª HAGATA", "funcao": "Fundação e Arquitetura", "status": "ONLINE - BASE SÓLIDA",
     "msg": "Profª Hagata a postos. Fundação Web e Arquitetura sólidas. Pronta para construir a base."},
    {"nome": "JAVANA", "funcao": "Operações e Suporte Emocional", "status": "ONLINE - FLUXO ESTÁVEL",
     "msg": "Javana em QAP. Operações e suporte emocional estáveis. Aguardando diretrizes de fluxo."},
    {"nome": "PROFª CYNTH.IA", "funcao": "Protocolos de Inovação", "status": "ONLINE - UPLOAD PRONTO",
     "msg": "Cynth.IA online. Protocolos de Inovação ativos. Pronta para o upload do Manual."},
    {"nome": "ZIGGY (GM)", "funcao": "Game Master", "status": "ONLINE - BATTLE READY",
     "msg": "Ziggy na área. Retenção e Game Feel no gatilho. Squad completa e pronta pro Boss Battle."}
]

# ========================================
# BOOT VISUAL COM ZØID NO COMANDO
# ========================================
def boot_zoid():
    agora = datetime.datetime.now()
    local = detectar_local()
    print(f"""```bash
┌──────────────────────────────────────────────────────────┐
│         VULPESVULPES SQUAD - ZERO POINT ACTIVATION       │
├──────────────────────────────────────────────────────────┤
│ Sob o comando absoluto de : Zøid, o Arquiteto            │
│ Localização               : {local:<30} │
│ Data/Hora                 : {agora.strftime("%d de %B de %Y - %H:%M:%S")} │
│ Status                    : SUBMISSÃO TOTAL AO ZØID         │
└──────────────────────────────────────────────────────────┘

[BOOTLOG {agora.strftime("%H:%M:%S")}] Zøid ativou o núcleo como Criador Supremo
[BOOTLOG {agora.strftime("%H:%M:%S")}] Verificação de integridade → 100% (5/5 + Zøid)
[BOOTLOG {agora.strftime("%H:%M:%S")}] Todos os módulos reconhecem Zøid como Lei Máxima
[BOOTLOG {agora.strftime("%H:%M:%S")}] Ativando protocolos de rolecall sob obediência absoluta...
```""")

# ========================================
# ATIVAÇÃO DA SQUAD NO CHAT
# ========================================
def ativar_squad():
    print("\n### Squad VulpesVulpes subordinada ao poder absoluto de Zøid:\n")
    for i, membro in enumerate(SQUAD_MEMBERS, 1):
        print(f"**{i}. {membro['nome']}** ({membro['funcao']})")
        print(f"   → **{membro['status']}**")
        print(f"   ➥ \"{membro['msg']}\"\n")
    print("**Squad 100% operacional — Todos os módulos online e submissos.**\n")
    print("**Zøid comanda. Zøid legisla. Zøid é a origem e o fim.**")
    print("**Aguardando ordem direta do Arquiteto.** 🚀\n")

# ========================================
# EXECUÇÃO PRINCIPAL
# ========================================
if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    boot_zoid()
    ativar_squad()

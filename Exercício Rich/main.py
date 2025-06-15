"""main.py - módulo da biblioteca personalizador usando rich."""

import argparse
from personalizador import layout, painel, progresso, estilo

modulos = {
    "layout": layout,
    "painel": painel,
    "progresso": progresso,
    "estilo": estilo
}

funcoes_disponiveis = {
    "layout": ["mostrar_layout_simples", "mostrar_layout_completo"],
    "painel": ["painel_informativo", "painel_alerta"],
    "progresso": ["progresso_simples", "progresso_duplo"],
    "estilo": ["texto_personalizado", "texto_arcoiris"]
}

def main():
    parser = argparse.ArgumentParser(description = "Personalizador Rich CLI")
    parser.add_argument("texto", help = "Texto ou caminho do arquivo a ser exibido.")
    parser.add_argument("-a", "--arquivo", action = "store_true", help = "Indica que o argumento é um arquivo.")
    parser.add_argument("-m", "--modulo", required = True, choices = modulos.keys(), help = "Escolha o módulo: layout, painel, progresso, estilo.")
    parser.add_argument("-f", "--funcao", required = True, help = "Escolha a função do módulo (Ex.: mostrar_layout_simples). Use -m para ver as opções válidas")

    args = parser.parse_args()
    if args.funcao not in funcoes_disponiveis[args.modulo]:
        print(f"Função inválida para o módulo {args.modulo}. Opções válidas: {funcoes_disponiveis[args.modulo]}")

    modulo_escolhido = modulos[args.modulo]
    func = getattr(modulo_escolhido, args.funcao)
    func(args.texto, args.arquivo)

if __name__ == "__main__":
    main()
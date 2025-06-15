"""estilo.py - módulo da biblioteca personalizador usando rich."""

from rich.console import Console
from rich.text import Text
from pathlib import Path

console = Console()

def texto_estilizado(texto: str, isArquivo: bool = False):
    conteudo = Path(texto).read_text() if isArquivo else texto
    estilizado = Text(conteudo)
    estilizado.stylize("bold red", 0, len(conteudo) // 2)
    estilizado.stylize("italic green", len(conteudo) // 2)
    console.print(estilizado)

def texto_arcoiris(texto: str, isArquivo: bool = False):
    cores = ["red", "yellow", "green", "cyan", "blue", "magenta"]
    conteudo = Path(texto).read_text() if isArquivo else texto
    estilizado = Text()

    for i, c in enumerate(conteudo):
        estilizado.append(c, style = cores[i % len(cores)])
    console.print(estilizado)
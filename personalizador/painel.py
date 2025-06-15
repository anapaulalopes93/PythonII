"""painel.py - módulo da biblioteca personalizador usando rich."""

from rich.console import Console
from rich.panel import Panel
from pathlib import Path

console = Console()

def painel_informativo(texto: str, isArquivo: bool = False):
    conteudo = Path(texto).read_text() if isArquivo else texto
    console.print(Panel(conteudo, title = "Informação", subtitle = "Painel Informativo", expand = False))

def painel_lateral(texto: str, isArquivo: bool = False):
    conteudo = Path(texto).read_text() if isArquivo else texto
    console.print(Panel(conteudo, title = "[red]Alerta[/red]", subtitle = "Atenção!", expand = True))
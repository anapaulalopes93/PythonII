"""layout.py - módulo da biblioteca personalizador usando rich."""

from rich.console import Console
from rich.layout import Layout
from pathlib import Path

console = Console()

def mostrar_layout_simples(texto: str, isArquivo: bool = False):
    layout = Layout()
    layout.split_column(Layout(name = "header"), Layout(name = "body"))
    conteudo = Path(texto).read_text() if isArquivo else texto
    layout["header"].update("[bold magenta]Cabeçalho[/bold magenta]")
    layout["body".update(conteudo)]
    console.print(layout)

def mostrar_layout_completo(texto: str, isArquivo: bool = False):
    layout = Layout()
    layout.split_column(
        Layout(name = "topo", size = 3),
        Layout(name = "corpo", ratio = 1),
        Layout(name = "rodape", size = 3)
    )

    conteudo = Path(texto).read_text() if isArquivo else texto
    layout["topo".update("[bold green]TOPO[/bold green]")]
    layout["corpo"].update(conteudo)
    layout["rodape"].update("[italic cyan]Rodapé[/italic cyan]")
    console.print(layout)
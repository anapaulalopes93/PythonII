"""progresso.py - módulo da biblioteca personalizador usando rich."""

from rich.progress import Progress
from rich.console import Console
from time import sleep
from pathlib import Path

console = Console()

def progresso_simples(texto: str, isArquivo: bool = False):
    conteudo = Path(texto).read_text() if isArquivo else texto
    with Progress() as progress:
        tarefa = progress.add_task("Processando...", total = 100)
        while not progress.finished:
            progress.update(tarefa, advance = 10)
            sleep(0.1)
    console.print(f"[bold green]Concluído:[/bold green] {conteudo}")

def progresso_duplo(texto: str, isArquivo: bool = False):
    conteudo = Path(texto).read_text() if isArquivo else texto
    with Progress() as progress:
        tarefa1 = progress.add_task("Tarefa A", total = 50)
        tarefa2 = progress.add_task("Tarefa B", total = 75)
        while not progress.finished:
            progress.update(tarefa1, advance = 5)
            progress.update(tarefa2, advance = 8)
            sleep(0.1)
    console.print(f"[bold blue]Finalizado:[/bold blue] {conteudo}")
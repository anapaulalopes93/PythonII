import os

estrutura = {
    'personalizador': ['__init__.py', 'layout.py', 'painel.py', 'progresso.py', 'estilo.py'], '': ['main.py']
}

for pasta, arquivos in estrutura.items():
    if pasta and not os.path.exists(pasta):
        os.makedirs(pasta)
    for arquivo in arquivos:
        caminho = os.path.join(pasta, arquivo)
        if not os.path.exists(caminho):
            with open(caminho, 'w', encoding = 'utf-8') as f:
                if arquivo.endswith('.py') and arquivo != '__init__.py':
                    f.write(f'"""{arquivo} - módulo da biblioteca personalizador usando rich."""\n\n')

print("Estrutura de projetos criada com sucesso!")
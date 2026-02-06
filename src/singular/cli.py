""" cli do sistema """

import click
from pathlib import Path


def criar_pasta(caminho: Path):
    if not caminho.exists():
        caminho.mkdir(parents=True)
        click.echo(f"[OK] Pasta criada: {caminho}")
    else:
        click.echo(f"[SKIP] Pasta já existe: {caminho}")


@click.group()
def cli():
    """Ferramenta CLI do framework Singular"""
    pass


@cli.command()
@click.argument("nome")
def start(nome):
    """Cria a estrutura de projeto do app."""
    
    base = Path(nome)

    # Estrutura
    assets = base / "assets"
    controller = base / "controller"
    views = base / "views"
    index = views / "index"
    models = base / "models"

    # Criar pastas
    for pasta in [base, assets, controller, views, index, models]:
        criar_pasta(pasta)

    # Criar page.py
    page_file = index / "page.py"
    if not page_file.exists():
        page_file.write_text("""from singular import Component, View, Text, Button, Render, Style, Link

class Contador(Component):
    def __init__(self):
        super().__init__()
        self.state = {"count": 0}

    def increment(self, e):
        self.state["count"] += 1
        self.set_state(self.state)

    def render(self):
        return View(
            View(
                Text("Contador Simples Feito em Singular"),
                Button(
                    f"Contador: {self.state['count']}", 
                    on_click=self.increment,
                    style=Style(
                        padding="10px",
                        cursor="pointer",
                        border_radius="10px",
                        border="0",
                        background_color="rgb(0, 255, 255)",
                        font_weight="bold"
                    )
                ),
                Link(
                    "Sobre o Desenvolvedor",
                    reload=True,
                    href="https://ricardocayoca.onrender.com/",
                    new_tab=True,
                ),
                Link(
                    "Documentação",
                    reload=True,
                    href="https://pypi.org/project/singular-framework/",
                    new_tab=True,
                ),
                style=Style(
                    display="flex", 
                    flex_direction="column",
                    align_items="center",
                    gap="10px",
                    
                )
            ),
            style=Style(
                flex="1",
                display="flex",
                color="#FFF",
                background_color="#111",
                align_items="center",
                justify_content="center",
                flex_direction="column",
                padding="20px",
                
                
            )
        )

Render(Contador())
""")
        click.echo(f"[OK] Arquivo criado: {page_file}")

    # Criar __init__.py na raiz
    init_file = base / "__init__.py"
    if not init_file.exists():
        if nome == ".": nome = "singular"
        init_file.write_text(f"""# Inicialização do app
from singular import Singular


app = Singular(__name__, title="{nome}")
""")

        click.echo(f"[OK] Arquivo criado: {init_file}")


@cli.command()
@click.option("--debug", is_flag=True, default=True, help="Ativa o modo debug")
def run(debug):
    """Procura a instância Singular() e executa app.run()."""

    import os
    import importlib.util
    from .core import Singular

    click.echo("🔍 Procurando instância Singular no projeto...")

    # 1. procurar arquivos python no diretório atual
    arquivos_py = [f for f in os.listdir(".") if f.endswith(".py")]

    if not arquivos_py:
        click.echo("❌ Nenhum arquivo .py encontrado.")
        return

    instancia = None

    # 2. tentar carregar module por module
    for arquivo in arquivos_py:
        caminho = os.path.join(".", arquivo)

        spec = importlib.util.spec_from_file_location("modulo_temp", caminho)
        modulo = importlib.util.module_from_spec(spec)

        try:
            spec.loader.exec_module(modulo)
        except Exception as e:
            continue  # ignora módulos com erro

        # 3. procurar variáveis cuja instância seja Singular
        for nome, valor in vars(modulo).items():
            try:
                if isinstance(valor, Singular):
                    instancia = valor
                    click.echo(f"✅ Instância encontrada: {nome} em {arquivo}")
                    break
            except:
                pass

        if instancia:
            break

    if not instancia:
        click.echo("❌ Nenhuma instância Singular() encontrada no projeto.")
        return

    # 4. executar run()
    click.echo("🚀 Iniciando servidor...\n")
    instancia.run(debug=debug)



if __name__ == "__main__":
    cli()

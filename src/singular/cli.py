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
    pages  = base / "pages"

    # Criar pastas
    for pasta in [base, assets, pages]:
        criar_pasta(pasta)

    # Criar page.py
    page_file = pages / "page.py"
    if not page_file.exists():
        page_file.write_text("""from singular import *



class Button(Link):
    def __init__(self, text, link, target=""):
        super().__init__(
            elements=[
                Text(text, style=Style(font_size=".8rem"))
            ],
            style=Style(
                background_color="#000000",
                padding="10px",
                text_decoration="None",
                border_radius="10px",
                color="#FFF",
            ),
            href=link,
            target=target
            
        )

@page()
def index():
    
    return View(
        elements=[
            Text(
                text="Singular FrameWork",
                style=Style(
                    font_weight="bold",
                    font_size="2rem"
                )
            ),
            Text("Singular é um framerwork full-stack simples para amantes da linguagem python"),
            View(
                elements=[
                    Button(text="Documentação", link="doc"),
                    Button(text="Portifolio do criador", link="https://ricardocayoca.onrender.com/", target="_blank")
                ],
                style=Style(
                    display="flex",
                    gap="20px",
                    align_items="center"
                )
            )
        ],
        className="side_bar",
        style=Style(
            display="flex",
            flex_direction="column",
            gap="10px",
            width="100%",
            height="100%",
            background_color="#333",
            justify_content="center",
            align_items="center",
            color="#FFF"
        )
    )


""")
        click.echo(f"[OK] Arquivo criado: {page_file}")

    # Criar __init__.py na raiz
    init_file = base / "__init__.py"
    if not init_file.exists():
        if nome == ".": nome = "singular"
        init_file.write_text(f"""# Inicialização do app
from singular import Singular


app = Singular(__name__)
""")

        click.echo(f"[OK] Arquivo criado: {init_file}")


@cli.command()
@click.option("--debug", is_flag=True, default=True, help="Ativa o modo debug")
def run(debug):
    """Procura a instância Singular() e executa app.run()."""

    import os
    import importlib.util
    from .core.core import Singular
    from .core.server import StandaloneAplication

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
    options = {
        "bind": "0.0.0.0:8500",
        "workers": 5,
        "--reload": True
    }
    
    #StandaloneAplication(instancia, options=options).run()
    instancia.run(debug=debug)



if __name__ == "__main__":
    cli()

# Singular Framework

**Singular** é um micro-framework declarativo em Python que permite construir aplicações web modernas utilizando apenas Python para estruturar backend e interface.

Ele abstrai a complexidade do Flask e fornece:

* Sistema de rotas baseado em arquivos
* Componentes declarativos
* Sistema de renderização centralizado
* Estrutura modular
* CLI integrada
* Integração com HTMX
* Sistema de estilos programático

---

# 🎯 Objetivo

O Singular foi criado para permitir que desenvolvedores construam aplicações web completas utilizando majoritariamente Python, reduzindo a necessidade de escrever grandes quantidades de HTML e CSS manualmente.

---

# 📁 Estrutura do Projeto

```
.
├── app.py
├── assets
└── pages
    ├── dashboard
    │   └── page.py
    ├── page.py
    └── produtos
        ├── [id]
        │   └── page.py
        └── page.py

```

---

# 🚀 Funcionalidades Principais

## 1️⃣ Sistema de Rotas Baseado em Arquivos

O Singular detecta automaticamente arquivos `page.py` dentro da pasta `pages` e registra rotas dinamicamente no Flask.
Para parametros dinamicos em url ex: /produto/1, basta colocar entre `[nome da pasta]` ou `<nome da pasta>` e o singular entende

└── produtos
        ├── [id]
        │   └── page.py # aqui a pagina que sera exibida com um parametro
        └── page.py

Exemplo:

```python
from singular import *

@page()
def index(req, id):
    return View(
        elements=[...]
    )
```

onde o id é o parametro da url e o req é a requisição que o flask passa a função

O decorator `@page()` registra automaticamente a rota correspondente ao arquivo.

### Benefícios:

* Organização automática
* Sem necessidade de registrar rotas manualmente
* Estrutura limpa e previsível

---

## 2️⃣ Decorador `@page`

O decorator `@page` define uma página renderizável.

Parâmetros suportados:

```python
@page(
    title:str=None,  
    stylesheet:StyleSheet=None, 
    middleware:Middleware=None, 
    methods=["GET"] 
)
```

### Permite:

* Css programatico
* Registro de middlewares **brevemente**
* Configuração da página **brevemente**
* Integração com layout base **brevemente**

---

## 3️⃣ Sistema de Renderização

O Singular utiliza um template base (`page.html`) e injeta o conteúdo da View dinamicamente.

Fluxo:

1. A função da página retorna uma `View`
2. O `render.py` processa o conteúdo
3. O template base é aplicado
4. A resposta final é enviada

Isso centraliza a renderização e mantém consistência visual.

---

## 4️⃣ Sistema de Componentes (UI)

Em `ui/components.py`, é possível criar componentes reutilizáveis.

Exemplo conceitual:

```python
Button("Salvar")
Card(content)
Container(children)
```

### Vantagens:

* Reutilização
* Código mais limpo
* Estrutura declarativa
* Separação clara entre lógica e interface

---

## 5️⃣ Engine de Elementos

O arquivo `_element.py` permite criar elementos HTML programaticamente.

Isso elimina a necessidade de escrever HTML manualmente e permite:

* Composição dinâmica
* Encadeamento de elementos
* Estrutura modular

---

## 6️⃣ Sistema de Estilos Programático

Com `_style.py`, é possível definir estilos via Python.

Isso facilita:

* Estilização dinâmica
* Padronização visual
* Organização de temas

---

## 7️⃣ Integração com HTMX [ possivel mas ainda não implemantado as 100%]

A integração com HTMX permite:

* Atualizações parciais de página
* Interações assíncronas
* Redução de JavaScript manual

Isso aproxima o Singular de frameworks modernos sem necessidade de SPA completo.

---

## 8️⃣ CLI Integrada

O arquivo `cli.py` fornece comandos para executar e gerenciar o projeto.

Possíveis comandos futuros:

```
singular start nome-do-projeto
singular run 
```

A CLI é o ponto de entrada oficial do framework.

---

# 🔐 Middleware (Planejado / Em Evolução)

O Singular suporta a ideia de middlewares declarativos:

```python
class Auth(Middleware):
    def after(self):
        ....

    def before(self):
        ...


@page(middleware=Auth)
```

Isso permite executar funções antes e depois da renderização da página.

Casos de uso:
s
* Autenticação
* Permissões
* Logging
* Validação

---

# 🧠 Filosofia do Framework

Singular segue os princípios:

* Declarativo
* Modular
* Minimalista
* Python-first
* Estrutura previsível

Ele busca reduzir complexidade sem perder poder.

---

# 📌 Diferenciais

✔ Rotas automáticas baseadas em arquivos
✔ UI declarativa em Python
✔ Integração com HTMX
✔ Arquitetura modular
✔ Foco em produtividade

---

# 🔮 Visão Futuramente

Possíveis evoluções:

* Sistema de layout aninhado
* Context global
* Sistema de estado
* Virtual DOM leve
* Build system próprio
* Independência do Flask

---

# 📦 Conclusão

Singular é um micro-framework que busca simplificar o desenvolvimento web com Python, oferecendo uma estrutura organizada, declarativa e produtiva.

Ele é ideal para:

* SaaS
* Dashboards
* Sistemas administrativos
* Aplicações internas
* MVPs rápidos

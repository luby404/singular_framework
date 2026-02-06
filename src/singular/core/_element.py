from ._style import Style

class Element:
    def __init__(self, name:str = "div", content: str = "", childs: list = None, style: Style = Style(), attrs: dict = {}):
        self.name = name
        self.content = content
        self.childs = childs or []
        self.style = style
        self.attrs = attrs or {}


        self.css_file = 0

    def add_child(self, element: "Element"):
        """Adiciona um elemento filho."""
        self.childs.append(element)

    def set_style(self, key: str, value: str):
        """Define ou altera um estilo CSS."""
        self.style[key] = value

    def set_attr(self, key: str, value: str):
        """Define ou altera um atributo HTML."""
        self.attrs[key] = value

    def _render_style(self):
        if not self.style:
            return ""
        return ' style="' + ";".join(f"{k}:{v}" for k, v in self.style.items()) + ';"'

    def _render_attrs(self):
        if not self.attrs:
            return ""
        return " " + " ".join(f'{k}="{v}"' for k, v in self.attrs.items())

    def render(self, indent: int = 0):
        """Renderiza o HTML final com indentação."""
        space = "  " * indent
        html = f"{space}<{self.name}{self._render_style()}{self._render_attrs()}>"

        if self.content:
            html += self.content

        if self.childs:
            html += "\n"
            for child in self.childs:
                html += child.render(indent + 1) + "\n"
            html += space

        html += f"</{self.name}>"
        return html






# ___ vai estar todos as classes de entrada de dados ___
from ..core._style import Style
from ..core._element import Element


from typing import Literal, Optional, Any
from functools import reduce


class BaseElement(Element):
    def __init__(self, name = "div", content = "", childs: Optional[Any] = None, style:Style= Style(), className:str="", id:str="", attrs:dict = {}):
        super().__init__(name, content, childs, style.style, attrs)

        # Adiciona class e id aos attrs, sobrescrevendo se já existirem
        self.attrs["class"] = className
        self.attrs["id"] = id
    
    def __str__(self):
        return self.render()


class View(BaseElement):
    def __init__(self, elements=[], style = Style(), className = "", id = "", attrs:dict = None):
        super().__init__(
            name="div",
            childs=list(elements),
            className=className,
            id=id,
            style=style,
            attrs=attrs
        )
    
class Text(BaseElement):
   def __init__(self, text:str="", style = Style(), className = "", id = "", attrs = {}):
       super().__init__(name="span", content=text, style=style, className=className, id=id, attrs=attrs)


class Link(BaseElement):
    def __init__(self, text:str="", href:str="", target="", style = Style(), className = "", id = "", attrs = {}, elements:list[BaseElement]=[]):
        super().__init__("a", text, elements, style, className, id, attrs)
        self.attrs = {}
        try: 
            self.attrs["href"] = href #url_for(href)
            self.attrs["target"] = target
        except: self.attrs["href"] = href
        


class Button(BaseElement):
    def __init__(self, text:str="", element:list[BaseElement]=[], onclick:callable=None, type:Literal["submit", "reset"]="submit", childs=None, style = Style(), className = "", id = "", attrs = {}):
        # Prioriza 'text' como content se não houver 'childs'
        self.id_element = ""
        if not childs and text:
            content = text
        else:
            content = ""
        
        attrs["type"] = type
        super().__init__("button", content, childs or element, style, className, id, attrs)
        
        # Mantendo self.childs = element, mas 'super' já trata isso
        self.attrs["onclick"] = "brython()"
        


class Input(BaseElement):
    def __init__(self, 
            type:Literal["file", "text", "submit", "search", "password", "checkbox", "number", "email", "hidden", "radio", "color", "date", "range"]="text", 
            placeholder:str="",
            name:str="",
            value:str="", # Adicionado
            required:bool=False, # Corrigido typo
            style = Style(), className = "", id = "", attrs = {}
        ):
        super().__init__(name="input", style=style, className=className, id=id, attrs=attrs)
        self.attrs["type"] = type
        self.attrs["name"] = name
        self.attrs["placeholder"] = placeholder
        self.attrs["value"] = value
        self.attrs["required"] = "required" if required else None # Padrão HTML para required

# Elemento Label para melhor acessibilidade
class Label(BaseElement):
    def __init__(self, text:str, for_input_id:str="", style = Style(), className = "", id = "", attrs = {}):
        super().__init__(name="label", content=text, style=style, className=className, id=id, attrs=attrs)
        self.attrs["for"] = for_input_id


class Image(BaseElement):
    def __init__(self, src:str="", alt:str="", style = Style(), className = "", id = "", attrs = {}): # Adicionado alt
        super().__init__(name="img", style=style, className=className, id=id, attrs=attrs)
        self.attrs["src"] = f"/assets?filename={src}"
        self.attrs["alt"] = alt


class Form(BaseElement):
    def __init__(self, action="", method:Literal["get", "post"]="get", style:Style=Style(), elements:list[BaseElement]=[], className:str=None, id:str=None):
        super().__init__(name="form", style=style, className=className, id=id)
        self.attrs["action"] = action
        self.attrs["method"] = method
        self.attrs["enctype"] = "multipart/form-data"

        self.childs = elements


class Option(BaseElement):
    """Representa a tag HTML <option> dentro de um ComboBox."""
    def __init__(self, text:str, value:str, selected:bool=False, style = Style(), className = "", id = "", attrs = {}):
        super().__init__(name="option", content=text, style=style, className=className, id=id, attrs=attrs)
        self.attrs["value"] = value
        if selected:
            self.attrs["selected"] = "selected"


class ComboBox(BaseElement):
    """Representa a tag HTML <select> para entrada de dados."""
    def __init__(self, 
            options:list[Option], 
            name:str="", 
            required:bool=False, 
            style = Style(), 
            className = "", 
            id = "", 
            attrs = {}
        ):
        super().__init__(name="select", childs=options, style=style, className=className, id=id, attrs=attrs)
        self.attrs["name"] = name
        self.attrs["required"] = "required" if required else None


class Table(BaseElement):
    def __init__(self, t_head:list=[], t_body:list=[], style = Style(display="flex"), className = "", id = "", attrs = {}):
        super().__init__(
            "table", "", 
            [
                BaseElement(name="th", childs=[
                    BaseElement(name="tr", childs=[ BaseElement(name="td", content=el) for el in t_head ]),
                ], style=Style(display="table-cell")),

                BaseElement(name="tbody", childs=[
                    BaseElement(name="tr", childs=[ BaseElement(name="td", content="wowo") for el in row ])
                    for row in t_body
                ], style=Style(display="table-cell")),

            ], 
            style, 
            className, 
            id, 
            attrs
        )

class TableIten(BaseElement):
    ...

class Modal(BaseElement):
    ...




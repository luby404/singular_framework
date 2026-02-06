from flask import render_template
from functools import wraps

def page(title:str=None, css_files:list=[], js_files:list=[]):
    """ retorna uma pagina html """
    
    def decorador(funcao:callable):
        @wraps(funcao)   # <-- ESSENCIAL
        def wrapper(*args, **kwargs):
            return render_template(
                "page.html",
                content=funcao(*args, **kwargs), 
                title=title if title else funcao.__name__,
                css_files=css_files,
                js_files=js_files
            )
        wrapper.__is_page__ = True
        return wrapper
    
    return decorador


def component():
    """ 
    retorna um view html para ser exibida no front-end
    target é onde o component sera renderizado 
    """
    def decorador(funcao):
        @wraps(funcao)
        def wrapper(*args, **kwargs):
            view = str(funcao(*args, **kwargs))
            return view
        wrapper.__is_component__ = True
        return wrapper
    
    return decorador


def action():
    return ...





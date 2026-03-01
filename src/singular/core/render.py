from flask import render_template, Request, make_response
from functools import wraps


from ..style import StyleSheet

def page( title:str=None,  stylesheet:StyleSheet=None,methods=["GET"] ):

    from flask import request
    
    def decorador(funcao:callable):
        
        @wraps(funcao)   # <-- ESSENCIAL
        
        def wrapper(*args, **kwargs):
            
            path = request.path
            _title = title if title else funcao.__name__
            if request.headers.get("HX-Request", False):
                resp = make_response(str(funcao(*args, **kwargs, req=request)))
                resp.headers["X-Page-Title"] = _title
                print(_title)
                return resp
            
            return render_template(
                "page.html",
                content="", 
                title=_title,
                stylesheet=stylesheet,
                path=path
            )
        wrapper.__is_page__ = True
        wrapper.methods = methods
        
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

def leyout():
    def decorador(funcao:callable):
        @wraps(funcao)   # <-- ESSENCIAL
        def wrapper(*args, **kwargs):
            return funcao(*args, **kwargs)
        
        wrapper.__is_leyout = True
        return wrapper
    return decorador



import os
from pathlib import Path
from flask import Flask, Blueprint, send_from_directory
from ..vars import BASE_PATH, APP_START_PATH, Route

from importlib import import_module
from importlib.util import spec_from_file_location, module_from_spec

from uuid import uuid4

class Router():
    
    def __init__(self, app:Flask, base_page:str):
        """ Encontrar as Blueprints nos arquivos """
        
        self.routes = {}
        self.app:Flask = app
        
        self.app_path = Path(APP_START_PATH)
        
        
        self.notfount_page = ""
        
        # buscar paginas
        for file in Path(APP_START_PATH).rglob("pages/**/*.py"):
            try:
                if file.name.endswith(".py") and file.is_file():
                    name_module = file.stem.replace(".", "_")
                    spec = spec_from_file_location(name_module, file)
                    module = module_from_spec(spec)
                    spec.loader.exec_module(module)
                    
                    for attr in dir(module):
                        obj = getattr(module, attr)
                        #if callable(obj) and attr == page.name.replace(".py", ""):
                        if callable(obj) and (getattr(obj, "__is_page__", False) or getattr(obj, "__is_component__", False)):
                            if file.name == "notfound.py":
                                self.notfount_page = obj                                
                            else:
                                prefix, url = self.gen_url(file, base_page)
                                #print(prefix, url)
                                
                                _route = {
                                    "route": url,
                                    "view": obj
                                }
                                
                                if prefix not in self.routes:
                                    self.routes[prefix] = []
                                
                                self.routes[prefix].append(Route(route=url, view=obj))
                
            except ValueError:
                continue
        
        for group, routes in self.routes.items():
            
            bp = Blueprint(group, __name__, url_prefix="/" if group == "index" else f"/{group}")
            for route in routes:
                #print(route)
                bp.add_url_rule(route.route, endpoint=str(uuid4()), view_func=route.view, strict_slashes=False)
                        
            app.register_blueprint(bp)
        
        app.add_url_rule("/assets/<path:filename>", view_func=self.assets)           
        
        # buscar pagina 404
        app.add_url_rule("/<path:path>", view_func=self.notFount )
        
        # add 404 page
        #(app.errorhandler(404))(lambda e: (self.notFount(e)))
          
    def gen_url(self, file, base_page):
        parts    = file.parts
        split    = str(Path(*parts[parts.index(base_page) + 1:])).replace(r"\\", "/").split("/")
        
        prefix = "index" if split[0].endswith(".py") else split[0]
        url = ""
        for i in split[1:split.index("page.py")]: 
            url += f"""/{i.replace("[", "<").replace("]", ">")}"""
        if url == "": url = "/"
        return prefix, url

    def assets(self, filename):
        base_app_name = os.path.join(APP_START_PATH, "assets")
        return send_from_directory(base_app_name, filename)

    def notFount(self, path):
        from flask import request as req
        
        page = "Pagina Não encontrada"
        
        if self.notfount_page:
            page = self.notfount_page()
        
        return page


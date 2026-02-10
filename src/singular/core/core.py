from flask import Flask
import os

from ..vars import BASE_PATH, APP_START_PATH
from .routes import Router

class Singular(Flask):
    def __init__(self, import_name, pages_dir:os.path="pages"):
        
        static_folder   = os.path.join(BASE_PATH,"ui", "static")
        template_folder = os.path.join(BASE_PATH,"ui", "templates")
        self.app_path = os.getcwd()
        self.routes = {}
        
        super().__init__(
            import_name=import_name, 
            static_folder=static_folder, 
            template_folder=template_folder, 
        )    
        
        Router(self, pages_dir)
        
        
    
    



from singular import *
from ui.sidebar import SideBar
from ui.style import leyout_base, content_style


@page()
def index(req):
    
    return View(
        elements=[
            SideBar(
                
            ),
            View(
                elements=[
                    Table(
                        thead=[
                            Text("Nome"), 
                            Text("Email"), 
                            Text("idade"), 
                            Text("Status")
                        ],
                        tbody=[
                            [
                                Text("Ricardo Cayoca"), 
                                Text("ricardokayoca@gmail.com"), 
                                Text("22"), 
                                Text("pendente")
                            ] for i in range(10)
                        ]
                    ),
                    Text(f"{req.url}")
                ],
                style=content_style
            )
        ],
        style=leyout_base
    )



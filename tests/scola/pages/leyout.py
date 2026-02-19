from singular import *


def leyout(element:View):
    
    return View(
        elements=[
            View(
                elements=[
                    Text("Header da pagina")
                ],
                
            ),
            element
        ]
    )
from singular import *






@page(stylesheet=style)
def dashboard(req:Request):
    
    return View(
        elements=[
            Text("Dashboard"),
            Link(text="ir para index", href="/")
        ]
    )


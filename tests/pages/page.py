from singular import *


style = StyleSheet(
    text=Style(   
        background_color="red"    
    ),
    button=Style(
        background_color="red",
        padding="10px"
    )
)

@page(stylesheet=style)
def index(req:Request):
    
    return View(
        elements=[
            Text("Pagina Index", className="text"),
            Link(
                text="ir para Dashboard", 
                className="button", 
                href="/dashboard"
            )
        ]
    )




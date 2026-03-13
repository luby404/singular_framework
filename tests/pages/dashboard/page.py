from singular import *


style = StyleSheet(
    text=Style(   
        background_color="green"    
    ),
    button=Style(
        background_color="blue",
        padding="10px"
    )
)



@page(stylesheet=style)
def dashboard(req:Request):
    
    return View(
        elements=[
            Text("Dashboard"),
            Link(text="ir para index", href="/", className="button")
        ]
    )


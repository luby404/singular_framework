from singular import *






@page(stylesheet=style)
def index(req:Request):
    
    return View(
        elements=[
            Text("Pagina Index"),
            Link(text="ir para Dashboard", href="/dashboard")
        ]
    )

style = StyleSheet(
    text=Style(
        
    )
)


print(style.style_sheet)


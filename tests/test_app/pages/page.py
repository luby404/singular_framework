from singular import *

@page(
    css_files=[
        "remix/remixicon.css"
    ]
)
def index():
    
    return View(
        elements=[
            Text("Pagina Home"),
            Link(text="Ir para dashboard", href="/dashboard/"),
        ],
        className="side_bar",
        style=Style(
            display="flex",
            flex_direction="column",
            gap="10px"
        )
    )
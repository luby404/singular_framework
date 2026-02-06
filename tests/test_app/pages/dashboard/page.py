from singular import *

from pages.dashboard.components.sidebar import SideBar, ItenMenu


@page(
    css_files=[
        "remix/remixicon.css",
        "dashboard.css"
    ]
)
def dashboard():
    
    return View(
        elements=[
            SideBar(
                iten=[
                    ItenMenu(icon="ri-function-line", label="Home"),
                    ItenMenu(icon="ri-file-list-line", label="Cargo"),
                    ItenMenu(icon="ri-group-line", label="Funcionarios"),
                    ItenMenu(icon="ri-line-chart-line", label="Salarios"),
                    ItenMenu(icon="ri-logout-box-r-line", label="Terminar Sessão")
                ]
            ),
            View(
                # content app
                elements=[],
                style=Style(
                    flex="1",
                    background_color="#FFF"
                )
            )
        ],
        style=Style(
            display="flex",
            width="100%",
            height="100%",
        )
    )




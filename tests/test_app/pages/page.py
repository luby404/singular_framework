from singular import *



class Button(Link):
    def __init__(self, text, link, target=""):
        super().__init__(
            elements=[
                Text(text, style=Style(font_size=".8rem"))
            ],
            style=Style(
                background_color="#000000",
                padding="10px",
                text_decoration="None",
                border_radius="10px",
                color="#FFF",
            ),
            href=link,
            target=target
            
        )

@page()
def index():
    
    return View(
        elements=[
            Text(
                text="Singular FrameWork",
                style=Style(
                    font_weight="bold",
                    font_size="2rem"
                )
            ),
            Text("Singular é um framerwork full-stack simples para amantes da linguagem python"),
            View(
                elements=[
                    Button(text="Documentação", link="doc"),
                    Button(text="Portifolio do criador", link="https://ricardocayoca.onrender.com/", target="_blank")
                ],
                style=Style(
                    display="flex",
                    gap="20px",
                    align_items="center"
                )
            )
        ],
        className="side_bar",
        style=Style(
            display="flex",
            flex_direction="column",
            gap="10px",
            width="100%",
            height="100%",
            background_color="#333",
            justify_content="center",
            align_items="center",
            color="#FFF"
        )
    )



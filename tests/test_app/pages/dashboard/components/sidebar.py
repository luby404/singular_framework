from singular import (
    View,
    Text,
    Link,
    Style
)


class ItenMenu(Link):
    def __init__(self, icon:str=None, label:str=None):
        super().__init__(
            elements=[
                Text(className=icon),
                Text(text=label)
            ],
            style=Style(
                text_decoration="none",
                color="#FFF",
                display="flex",
                gap="10px",
                padding="10px",
                border_radius="10px"
            ),
            className="iten_menu"
        )


class SideBar(View):
    def __init__(self, iten:list=[]):
        super().__init__(
            elements=[
                Link(
                    elements=[*iten]
                )
            ],
            style=content_side_bar_style
        )



content_side_bar_style = Style(
    width="200px",
    background_color="#333",
    padding="1rem",
    display="flex",
    flex_direction="column",
    gap="10px"
)
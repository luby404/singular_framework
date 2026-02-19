from singular import (
    View,
    Text,
    Link,
    Style
    
)

class SideBar(View):
    def __init__(self):
        super().__init__(
            elements=[
                
            ],
            style=style_side_bar
        )
        


style_side_bar = Style(
    background_color="#333",
    padding="10px",
    width="200px",
    border_radius="10px"
)
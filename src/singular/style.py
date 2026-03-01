from .core._style import Style

class StyleSheet():
    def __init__(self, **object_style:Style):
        self.style_sheet = {}

        for key, style in object_style.items():
            self.style_sheet[key] = style.to_block(key)





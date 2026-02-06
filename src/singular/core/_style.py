from typing import Literal
import inspect
import uuid


# gerar um arquivo css

class Style:
    def __init__(
        self,
        
        # ---------------- DISPLAY & VISIBILITY ----------------
        display: Literal["block", "inline", "inline-block", "flex", "grid", "none", "list-item", "table", "table-row", "table-cell"] = "block",
        visibility: Literal["visible", "hidden", "collapse"] = None,
        overflow: Literal["visible", "hidden", "scroll", "auto"] = None,
        overflow_x: Literal["visible", "hidden", "scroll", "auto"] = None,
        overflow_y: Literal["visible", "hidden", "scroll", "auto"] = None,
        float: Literal["left", "right", "none"] = None, # Adicionado
        clear: Literal["none", "left", "right", "both"] = None, # Adicionado
        
        # ---------------- FLEXBOX ----------------
        flex: str = None,
        flex_direction: Literal["row", "row-reverse", "column", "column-reverse"] = None,
        flex_wrap: Literal["nowrap", "wrap", "wrap-reverse"] = None,
        flex_grow: str = None, # Adicionado
        flex_shrink: str = None, # Adicionado
        flex_basis: str = None, # Adicionado
        order: str = None, # Adicionado
        justify_content: Literal["flex-start", "flex-end", "center", "space-between", "space-around", "space-evenly"] = None,
        align_items: Literal["flex-start", "flex-end", "center", "stretch", "baseline"] = None,
        align_content: Literal["flex-start", "flex-end", "center", "stretch", "space-between", "space-around"] = None,
        align_self: Literal["auto", "flex-start", "flex-end", "center", "stretch", "baseline"] = None, # Adicionado

        # ---------------- GRID ----------------
        grid_template_columns: str = None,
        grid_template_rows: str = None,
        grid_template_areas: str = None, # Adicionado
        grid_auto_columns: str = None, # Adicionado
        grid_auto_rows: str = None, # Adicionado
        grid_auto_flow: Literal["row", "column", "row dense", "column dense"] = None, # Adicionado
        grid_column: str = None,
        grid_row: str = None,
        grid_column_start: str = None, # Adicionado
        grid_column_end: str = None, # Adicionado
        grid_row_start: str = None, # Adicionado
        grid_row_end: str = None, # Adicionado
        grid_area: str = None, # Adicionado
        grid_gap: str = None,
        gap: str = None, # Para grid e flexbox

        # ---------------- POSITIONING ----------------
        position: Literal["static", "relative", "absolute", "fixed", "sticky"] = None,
        top: str = None,
        bottom: str = None,
        left: str = None,
        right: str = None,
        z_index: str = None,
        
        # ---------------- BOX MODEL ----------------
        width: str = None,
        height: str = None,
        min_width: str = None,
        max_width: str = None,
        min_height: str = None,
        max_height: str = None,
        margin: str = None,
        margin_top: str = None,
        margin_bottom: str = None,
        margin_left: str = None,
        margin_right: str = None,
        padding: str = None,
        padding_top: str = None,
        padding_bottom: str = None,
        padding_left: str = None,
        padding_right: str = None,
        box_sizing: Literal["content-box", "border-box"] = None, # Adicionado

        # ---------------- BORDER ----------------
        border: str = None,
        border_top: str = None,
        border_bottom: str = None,
        border_left: str = None,
        border_right: str = None,
        border_color: str = None,
        border_width: str = None,
        border_style: Literal["none", "hidden", "dotted", "dashed", "solid", "double", "groove", "ridge", "inset", "outset"] = None,
        border_radius: str = None,
        border_top_left_radius: str = None, # Adicionado
        border_top_right_radius: str = None, # Adicionado
        border_bottom_left_radius: str = None, # Adicionado
        border_bottom_right_radius: str = None, # Adicionado

        # ---------------- BACKGROUND ----------------
        background: str = None,
        background_color: Literal["transparent"] = None,
        background_image: str = None,
        background_size: str = None,
        background_position: str = None,
        background_repeat: str = None,
        background_attachment: Literal["scroll", "fixed", "local"] = None, # Adicionado
        background_clip: Literal["border-box", "padding-box", "content-box"] = None, # Adicionado
        
        # ---------------- TYPOGRAPHY ----------------
        color: str = None,
        font_size: str = None,
        font_weight: Literal["normal", "bold", "bolder", "lighter", "100", "200", "300", "400", "500", "600", "700", "800", "900"] = None, # Adicionado valores numéricos
        font_family: str = None,
        font_style: Literal["normal", "italic", "oblique"] = None, # Adicionado
        text_align: Literal["left", "right", "center", "justify"] = None,
        text_transform: Literal["none", "capitalize", "uppercase", "lowercase"] = None,
        text_decoration: str = None, # Usa a forma curta: underline, overline, line-through
        text_decoration_line: Literal["none", "underline", "overline", "line-through"] = None, # Adicionado (forma longa)
        text_decoration_color: str = None, # Adicionado
        text_shadow: str = None, # Adicionado
        white_space: Literal["normal", "nowrap", "pre", "pre-wrap", "pre-line"] = None, # Adicionado
        word_break: Literal["normal", "break-all", "keep-all", "break-word"] = None, # Adicionado
        line_height: str = None,
        letter_spacing: str = None,

        # ---------------- LISTS ----------------
        list_style: str = None, # Adicionado
        list_style_type: Literal["disc", "circle", "square", "decimal", "none"] = None, # Adicionado
        list_style_position: Literal["inside", "outside"] = None, # Adicionado

        # ---------------- TABLES ----------------
        border_collapse: Literal["collapse", "separate"] = None,
        border_spacing: str = None, # Adicionado
        caption_side: Literal["top", "bottom"] = None, # Adicionado
        empty_cells: Literal["show", "hide"] = None, # Adicionado
        table_layout: Literal["auto", "fixed"] = None, # Adicionado

        # ---------------- EFFECTS & INTERACTIVITY ----------------
        opacity: str = None,
        box_shadow: str = None,
        filter: str = None,
        pointer_events: Literal["auto", "none"] = None, # Adicionado
        resize: Literal["none", "both", "horizontal", "vertical"] = None, # Adicionado

        # ---------------- TRANSITION & ANIMATION ----------------
        transition: str = None,
        transition_property: str = None, # Adicionado
        transition_duration: str = None, # Adicionado
        transition_timing_function: str = None, # Adicionado
        transition_delay: str = None, # Adicionado
        transform: str = None,
        transform_origin: str = None, # Adicionado
        animation: str = None,
        animation_name: str = None, # Adicionado
        animation_duration: str = None,
        animation_timing_function: str = None,
        animation_delay: str = None,
        animation_iteration_count: str = None,
        animation_direction: str = None,
        animation_fill_mode: str = None,
        animation_play_state: Literal["paused", "running"] = None, # Adicionado
        
        # ---------------- CURSOR ----------------
        cursor: Literal["auto", "default", "none", "context-menu", "help", "pointer", "progress", "wait", "cell", "crosshair", "text", "vertical-text", "alias", "copy", "move", "no-drop", "not-allowed", "grab", "grabbing", "e-resize", "n-resize", "ne-resize", "nw-resize", "s-resize", "se-resize", "sw-resize", "w-resize", "col-resize", "row-resize", "all-scroll", "zoom-in", "zoom-out"] = None, # Expansão da lista
        
        # ---------------- OUTROS ----------------
        outline: str = None,
        outline_color: str = None, # Adicionado
        outline_style: str = None, # Adicionado
        outline_width: str = None, # Adicionado
        
        **keyargs
    ):

        args = inspect.getfullargspec(self.__init__).args
        # self.data_attr_ armazena apenas os argumentos que NÃO são None
        self.data_attr_ = {
            arg: locals()[arg] for arg in args if arg != "self" and locals()[arg] is not None
        }

        self.style          = self.render_style()
        self.style_selector = str(uuid.uuid4())

    def render_style(self):
        style_str = {}
        for k, v in self.data_attr_.items():
            # Converte snake_case (Python) para kebab-case (CSS)
            k = k.replace("_", "-")
            style_str[k] = v
        return style_str

    def to_inline(self) -> str:
        return "; ".join(f"{k}: {v}" for k, v in self.style.items())

    def to_block(self, selector: str) -> str:
        css = f"{selector} {{\n"
        for k, v in self.style.items():
            css += f"  {k}: {v};\n"
        css += "}"
        return css
    
    def __str__(self):
        # Gera uma string CSS no formato 'propriedade: valor; propriedade: valor;'
        return "; ".join([f"{k}: {v}" for k, v in self.style.items()])


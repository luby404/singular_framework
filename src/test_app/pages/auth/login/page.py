from singular import (
    View,
    Text,
    page
)

@page()
def index():
    return View(
        Text("Olá, Mundo")
    )
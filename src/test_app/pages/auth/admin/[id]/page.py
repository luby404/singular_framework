from singular import (
    View,
    Text,
    page
)

@page()
def index(id):
    return View(
        Text(f"id:{id}")
    )
    
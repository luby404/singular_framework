from singular import View, Text, page

@page()
def posts(req, id):
    
    return View(
        elements=[
            Text(f"detalhe do post {id}")
        ],
    )



from singular import View, Text, page, Request

@page()
def posts(req: Request):
    
    return View(
        elements=[
            *[
                Text(f"Post {i}") for i in range(10)
            ],
            Text(f"{req.path}")
        ]
    )
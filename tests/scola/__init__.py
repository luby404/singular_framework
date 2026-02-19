# Inicialização do app
from singular import Singular


app = Singular(__name__)

app.run(
    debug=True
)

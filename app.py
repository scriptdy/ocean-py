from flask import Flask, render_template

app = Flask(__name__) 

# POST MOCK
posts = [
    {
        "titulo": "Post 1",
        "texto": "Meu primeiro post"
    },
    {
        "titulo": "Post 2",
        "texto": "Segundo Post"
    },
        {
        "titulo": "Post 3",
        "texto": "Novo Post"
    },
]

@app.route('/')
def exibir_entradas():

    return render_template("exibir_entradas.html", entradas=posts)
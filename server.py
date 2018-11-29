from bottle import run, get, post, view, request, redirect

desafio = "Quero ver voce digitar isso tudo"
pos = 0
textUser = ""

def compara(textUser, desafio, pos, code):
    ultimo = len(textUser) - 1
    if (code == desafio[pos]):
        textUser = textUser + code
        return pos + 1, textUser
    return pos, textUser
    
@post('/')
def index():
    return desafio

@post('/usr/<name>/put/<code>')
def teste(name, code):
    global textUser
    global pos
    pos, textUser = compara(textUser, desafio, pos, code)
    return textUser

@post('/usr/<name>/digit/<qtd>')
def teste(name, qtd):
    global textUser
    global pos
    textUser = ""
    pos = 0
    return "Parabens {}, voce digitou a frase completa!".format(name)

run(host='localhost', port=8080)

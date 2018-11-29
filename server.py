import bottle
from bottle import run, get, post, view, request, redirect
import requests
import json
import threading
import time
import sys

peers = sys.argv[2:]

desafio = "Quero ver voce digitar isso tudo"
pos = 0
textUser = ""

@bottle.route('/peers/<porta>')
def index(porta):
    peers.append(porta)
    peers[:] = list(set(peers))
    return json.dumps(peers)

def client():
    time.sleep(5)
    while True:
        time.sleep(1)
        np = []
        for p in peers:
            if p == sys.argv[1]:
                continue
            r = requests.get('http://localhost:' + p + '/peers/'+sys.argv[1])
            np = np + json.loads(r.text)
            time.sleep(1)
        peers[:] = list(set(np + peers))


@bottle.route('/texts')
def index():
    return json.dumps(textUser)

def client_text():
    global textUser
    global pos
    time.sleep(5)
    while True:
        time.sleep(1)
        for p in peers:
            if p == sys.argv[1]:
                continue
            r = requests.get('http://localhost:' + p + '/texts')
            tmp_text = json.loads(r.text)
            time.sleep(1)
            #print(tmp_pos, tmp_text)
            print(pos, textUser)
            if len(tmp_text) > len(textUser):
                pos = len(tmp_text)
                textUser = tmp_text

def compara(textUser, desafio, pos, code):
    if (len(textUser) == len(desafio)):
        return len(textUser), textUser
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
    #textUser = ""
    #pos = 0
    return "Parabens {}, voce digitou a frase completa!".format(name)


t = threading.Thread(target=client)
t.start()

t2 = threading.Thread(target=client_text)
t2.start()

run(host='localhost', port=int(sys.argv[1]))

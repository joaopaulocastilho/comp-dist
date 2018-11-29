import requests
import sys

nome = sys.argv[1]
porta = sys.argv[2]
pos = 0

def getChar():
    try:
        # for Windows-based systems
        import msvcrt # If successful, we are on Windows
        return msvcrt.getch()

    except ImportError:
        # for POSIX-based systems (with termios & tty support)
        import tty, sys, termios  # raises ImportError if unsupported
        fd = sys.stdin.fileno()
        oldSettings = termios.tcgetattr(fd)
        try:
            tty.setcbreak(fd)
            answer = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, oldSettings)
        return answer

r = requests.post('http://localhost:8080')
desafio = str(r.text)
print(desafio)

tam = 0
while tam < len(desafio):
    tmp = getChar()
    r1 = requests.post('http://localhost:{}/usr/{}/put/{}'.format(porta, nome, tmp))
    meuTexto = str(r1.text)
    tam = len(meuTexto)
    print(meuTexto)

r2 = requests.post('http://localhost:{}/usr/{}/digit/{}'.format(porta, nome, tam))
print(r2.text)

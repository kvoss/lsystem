import turtle
from lsystem import LSystem

plant = dict(
        axiom = 'X',
        rules = {'X': 'F-[[X]+]+F[+FX]-X', 'F':'FF'})
plantL = LSystem(**plant)


q = []
def restore():
    tv = q.pop()
    turtle.up()
    turtle.setposition(tv[0])
    turtle.seth(tv[1])
    turtle.down()

methods = {
        'F': lambda: turtle.fd(3),
        '-': lambda: turtle.left(25),
        '+': lambda: turtle.right(25),

        '[': lambda: q.append((turtle.pos(), turtle.heading())),
        ']': restore,

        'A': lambda: turtle.fd(5),
        'B': lambda: turtle.fd(2),
}

turtle.ht()
turtle.pencolor('green')
turtle.delay(0)
turtle.seth(90)
for c in plantL[5]:
    try:
        methods[c]()
    except KeyError:
        pass

turtle.exitonclick()


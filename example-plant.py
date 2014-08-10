import turtle
from lsystem import LSystem

plant = dict(
        axiom = 'X',
        rules = {'X': 'F-[[X]+X]+F[+FX]-X', 'F':'FF'})
plantL = LSystem(**plant)


q = []
def restore():
    tv = q.pop()
    turtle.up()
    turtle.setposition(tv[0])
    turtle.seth(tv[1])
    turtle.down()

methods = {
        'F': lambda: turtle.fd(2),
        '-': lambda: turtle.left(25),
        '+': lambda: turtle.right(25),

        '[': lambda: q.append((turtle.pos(), turtle.heading())),
        ']': restore,
}

turtle.ht()
turtle.pencolor('green')
turtle.delay(0)
turtle.seth(75)
for c in plantL[6]:
    try:
        methods[c]()
    except KeyError:
        pass

turtle.exitonclick()

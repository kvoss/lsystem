import turtle
from lsystem import LSystem

koch_curve = dict(
        variables = ['F'],
        consts = ['+', '-'],
        axiom = 'F',
        rules = {'F': 'F+F-F-F-F-F', '-': '-F-+'})
koch_curveL = LSystem(**koch_curve)

methods = {
        'F': lambda: turtle.fd(2),
        '+': lambda: turtle.left(90),
        '-': lambda: turtle.right(90),
}

turtle.ht()
turtle.delay(1)
for c in koch_curveL[5]:
    try:
        methods[c]()
    except KeyError:
        pass

turtle.exitonclick()

